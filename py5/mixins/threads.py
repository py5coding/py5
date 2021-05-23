# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2021 Jim Schmitz
#
#   This library is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 2.1 of the License, or (at
#   your option) any later version.
#
#   This library is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
#   General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this library. If not, see <https://www.gnu.org/licenses/>.
#
# *****************************************************************************
import sys
import time
import threading
from collections.abc import Iterable
from typing import Callable, Dict, Tuple, Any

from .. import methods


class Py5Promise:

    def __init__(self):
        self._result = None
        self._is_ready = False

    @property
    def is_ready(self) -> bool:
        return self._is_ready

    @property
    def result(self) -> Any:
        return self._result

    def _set_result(self, result):
        self._result = result
        self._is_ready = True


class Py5Thread:

    def __init__(self, sketch, f, args, kwargs):
        self.sketch = sketch
        self.f = f
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        pass

    def __call__(self):
        try:
            self.f(*self.args, **self.kwargs)
        except Exception:
            methods.handle_exception(*sys.exc_info())
            self.sketch._terminate_sketch()


class Py5PromiseThread(Py5Thread):

    def __init__(self, sketch, f, promise, args, kwargs):
        super().__init__(sketch, f, args, kwargs)
        self.promise = promise

    def stop(self):
        super().stop()

    def __call__(self):
        try:
            self.promise._set_result(self.f(*self.args, **self.kwargs))
        except Exception:
            methods.handle_exception(*sys.exc_info())
            self.sketch._terminate_sketch()


class Py5RepeatingThread(Py5Thread):

    def __init__(self, sketch, f, delay, args, kwargs):
        super().__init__(sketch, f, args, kwargs)
        self.repeat = True
        self.delay = delay
        self.e = threading.Event()

    def stop(self):
        super().stop()
        self.repeat = False
        self.e.set()

    def __call__(self):
        try:
            while self.repeat:
                start_time = time.time()
                self.f(*self.args, **self.kwargs)
                self.e.wait(max(0, start_time + self.delay - time.time()))
        except Exception:
            self.stop()
            methods.handle_exception(*sys.exc_info())
            self.sketch._terminate_sketch()


class ThreadsMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._py5threads = {}

    def _check_param_types(self, args, kwargs):
        if not isinstance(args, Iterable) and args is not None:
            raise RuntimeError(
                'args argument must be iterable (such as a tuple or list)')
        if not isinstance(kwargs, dict) and kwargs is not None:
            raise RuntimeError('kwargs argument must be a dictionary')

        kwargs = kwargs or {}
        args = args or ()

        return args, kwargs

    def _launch_py5thread(self, name, py5thread, daemon):
        if self.has_thread(name):
            self.stop_thread(name, wait=True)

        t = threading.Thread(name=name, target=py5thread, daemon=daemon)
        t.start()
        self._py5threads[t.name] = (t, py5thread)

        return t.name

    def _shutdown(self):
        self.stop_all_threads(wait=False)
        super()._shutdown()

    # *** BEGIN METHODS ***

    def launch_thread(
            self,
            f: Callable,
            name: str = None,
            *,
            daemon: bool = True,
            args: Tuple = None,
            kwargs: Dict = None) -> str:
        """Launch a new thread to execute a function in parallel with your Sketch code.

        Parameters
        ----------

        args: Tuple = None
            positional arguments to pass to the given function

        daemon: bool = True
            if the thread should be a daemon thread

        f: Callable
            function to call in the launched thread

        kwargs: Dict = None
            keyword arguments to pass to the given function

        name: str = None
            name of thread to be created

        Notes
        -----

        Launch a new thread to execute a function in parallel with your Sketch code.
        This can be useful for executing non-py5 code that would otherwise slow down the
        animation thread and reduce the Sketch's frame rate.

        The ``name`` parameter is optional but useful if you want to monitor the thread
        with other methods such as ``has_thread()``. If the provided ``name`` is
        identical to an already running thread, the running thread will first be stopped
        with a call to ``stop_thread()`` with the ``wait`` parameter equal to ``True``.

        Use the ``args`` and ``kwargs`` parameters to pass positional and keyword
        arguments to the function.

        Use the ``daemon`` parameter to make the launched thread a daemon that will run
        without blocking Python from exiting. This parameter defaults to ``True``,
        meaning that function execution can be interupted if the Python process exits.
        Note that if the Python process continues running after the Sketch exits, which
        is typically the case when using a Jupyter Notebook, this parameter won't have
        any effect unless if you try to restart the Notebook kernel. Generally speaking,
        setting this parameter to ``False`` causes problems but it is available for
        those who really need it. See ``stop_all_threads()`` for a better approach to
        exit threads.

        The new thread is a Python thread, so all the usual caveats about the Global
        Interpreter Lock (GIL) apply here."""
        args, kwargs = self._check_param_types(args, kwargs)
        return self._launch_py5thread(
            name, Py5Thread(
                self, f, args, kwargs), daemon)

    def launch_promise_thread(
            self,
            f: Callable,
            name: str = None,
            *,
            daemon: bool = True,
            args: Tuple = None,
            kwargs: Dict = None) -> Py5Promise:
        """Create a ``Py5Promise`` object that will store the returned result of a function
        when that function completes.

        Parameters
        ----------

        args: Tuple = None
            positional arguments to pass to the given function

        daemon: bool = True
            if the thread should be a daemon thread

        f: Callable
            function to call in the launched thread

        kwargs: Dict = None
            keyword arguments to pass to the given function

        name: str = None
            name of thread to be created

        Notes
        -----

        Create a ``Py5Promise`` object that will store the returned result of a function
        when that function completes. This can be useful for executing non-py5 code that
        would otherwise slow down the animation thread and reduce the Sketch's frame
        rate.

        The ``Py5Promise`` object has an ``is_ready`` property that will be ``True``
        when the ``result`` property contains the value function ``f`` returned. Before
        then, the ``result`` property will be ``None``.

        The ``name`` parameter is optional but useful if you want to monitor the thread
        with other methods such as ``has_thread()``. If the provided ``name`` is
        identical to an already running thread, the running thread will first be stopped
        with a call to ``stop_thread()`` with the ``wait`` parameter equal to ``True``.

        Use the ``args`` and ``kwargs`` parameters to pass positional and keyword
        arguments to the function.

        Use the ``daemon`` parameter to make the launched thread a daemon that will run
        without blocking Python from exiting. This parameter defaults to ``True``,
        meaning that function execution can be interupted if the Python process exits.
        Note that if the Python process continues running after the Sketch exits, which
        is typically the case when using a Jupyter Notebook, this parameter won't have
        any effect unless if you try to restart the Notebook kernel. Generally speaking,
        setting this parameter to ``False`` causes problems but it is available for
        those who really need it. See ``stop_all_threads()`` for a better approach to
        exit threads.

        The new thread is a Python thread, so all the usual caveats about the Global
        Interpreter Lock (GIL) apply here."""
        args, kwargs = self._check_param_types(args, kwargs)
        promise = Py5Promise()
        self._launch_py5thread(
            name, Py5PromiseThread(
                self, f, promise, args, kwargs), daemon)
        return promise

    def launch_repeating_thread(
            self,
            f: Callable,
            name: str = None,
            *,
            time_delay: float = 0,
            daemon: bool = True,
            args: Tuple = None,
            kwargs: Dict = None) -> str:
        """Launch a new thread that will repeatedly execute a function in parallel with
        your Sketch code.

        Parameters
        ----------

        args: Tuple = None
            positional arguments to pass to the given function

        daemon: bool = True
            if the thread should be a daemon thread

        f: Callable
            function to call in the launched thread

        kwargs: Dict = None
            keyword arguments to pass to the given function

        name: str = None
            name of thread to be created

        time_delay: float = 0
            time delay in seconds between calls to the given function

        Notes
        -----

        Launch a new thread that will repeatedly execute a function in parallel with
        your Sketch code. This can be useful for executing non-py5 code that would
        otherwise slow down the animation thread and reduce the Sketch's frame rate.

        Use the ``time_delay`` parameter to set the time in seconds between one call to
        function ``f`` and the next call. Set this parameter to ``0`` if you want each
        call to happen immediately after the previous call finishes. If the function
        ``f`` takes longer than expected to finish, py5 will wait for it to finish
        before making the next call. There will not be overlapping calls to function
        ``f``.

        The ``name`` parameter is optional but useful if you want to monitor the thread
        with other methods such as ``has_thread()``. If the provided ``name`` is
        identical to an already running thread, the running thread will first be stopped
        with a call to ``stop_thread()`` with the ``wait`` parameter equal to ``True``.

        Use the ``args`` and ``kwargs`` parameters to pass positional and keyword
        arguments to the function.

        Use the ``daemon`` parameter to make the launched thread a daemon that will run
        without blocking Python from exiting. This parameter defaults to ``True``,
        meaning that function execution can be interupted if the Python process exits.
        Note that if the Python process continues running after the Sketch exits, which
        is typically the case when using a Jupyter Notebook, this parameter won't have
        any effect unless if you try to restart the Notebook kernel. Generally speaking,
        setting this parameter to ``False`` causes problems but it is available for
        those who really need it. See ``stop_all_threads()`` for a better approach to
        exit threads.

        The new thread is a Python thread, so all the usual caveats about the Global
        Interpreter Lock (GIL) apply here."""
        args, kwargs = self._check_param_types(args, kwargs)
        return self._launch_py5thread(
            name, Py5RepeatingThread(
                self, f, time_delay, args, kwargs), daemon)

    def _remove_dead_threads(self):
        thread_names = list(self._py5threads.keys())
        for t_name in thread_names:
            if not self._py5threads[t_name][0].is_alive():
                del self._py5threads[t_name]

    def has_thread(self, name: str) -> None:
        """Determine if a thread of a given name exists and is currently running.

        Parameters
        ----------

        name: str
            name of thread

        Notes
        -----

        Determine if a thread of a given name exists and is currently running. You can
        get the list of all currently running threads with ``list_threads()``."""
        self._remove_dead_threads()
        return name in self._py5threads

    def stop_thread(self, name: str, wait: bool = False) -> None:
        """Stop a thread of a given name.

        Parameters
        ----------

        name: str
            name of thread

        wait: bool = False
            wait for thread to exit before returning

        Notes
        -----

        Stop a thread of a given name. The ``wait`` parameter determines if the method
        call will return right away or wait for the thread to exit.

        This won't do anything useful if the thread was launched with either
        ``launch_thread()`` or ``launch_promise_thread()`` and the ``wait`` parameter is
        ``False``. Non-repeating threads are executed once and will stop when they
        complete execution. Setting the ``wait`` parameter to ``True`` will merely block
        until the thread exits on its own. Killing off a running thread in Python is
        complicated and py5 cannot do that for you. If you want a thread to perform some
        action repeatedly and be interuptable, use ``launch_repeating_thread()``
        instead.

        Use ``has_thread()`` to determine if a thread of a given name exists and
        ``list_threads()`` to get a list of all thread names. Use ``stop_all_threads()``
        to stop all threads."""
        if name in self._py5threads:
            t, py5thread = self._py5threads[name]
            py5thread.stop()
            if wait:
                t.join()

    def stop_all_threads(self, wait: bool = False) -> None:
        """Stop all running threads.

        Parameters
        ----------

        wait: bool = False
            wait for thread to exit before returning

        Notes
        -----

        Stop all running threads. The ``wait`` parameter determines if the method call
        will return right away or wait for the threads to exit.

        When the Sketch shuts down, ``stop_all_threads(wait=False)`` is called for you.
        If you would rather the Sketch waited for threads to exit, create an ``exiting``
        method and make a call to ``stop_all_threads(wait=True)``."""
        current_thread_name = threading.current_thread().name
        for name in self.list_threads():
            if name == current_thread_name:
                # don't try to join a thread with itself
                continue
            self.stop_thread(name, wait=wait)

    def list_threads(self) -> None:
        """List the names of all of the currently running threads.

        Notes
        -----

        List the names of all of the currently running threads. The names of previously
        launched threads that have exited will be removed from the list."""
        self._remove_dead_threads()
        return list(self._py5threads.keys())
