# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2023 Jim Schmitz
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
from __future__ import annotations

import functools
import weakref

from jpype.types import JInt, JChar

from . import spelling


def _convert_jchar_to_chr(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        result = f(self_, *args)
        if isinstance(result, JChar):
            result = chr(result)
        return result
    return decorated


def _convert_jint_to_int(f):
    @functools.wraps(f)
    def decorated(self_, *args):
        result = f(self_, *args)
        if isinstance(result, JInt):
            result = int(result)
        return result
    return decorated


class Py5KeyEvent:
    """Datatype for providing information about key events.

    Underlying Processing class: KeyEvent.KeyEvent

    Notes
    -----

    Datatype for providing information about key events. An instance of this class
    will be passed to user-defined key event functions if py5 detects those
    functions accept 1 (positional) argument, as demonstrated in the example code.
    The key event functions can be any of `key_pressed()`, `key_typed()`, or
    `key_released()`. Key events can be generated faster than the frame rate of the
    Sketch, making key event functions useful for capturing all of a user's keyboard
    activity.
    """
    _py5_object_cache = weakref.WeakSet()

    def __new__(cls, pkeyevent):
        for o in cls._py5_object_cache:
            if pkeyevent == o._instance:
                return o
        else:
            o = object.__new__(Py5KeyEvent)
            o._instance = pkeyevent
            cls._py5_object_cache.add(o)
            return o

    def __str__(self):
        key = self.get_key()
        action = self.get_action()

        action_str = 'UNKNOWN'
        for k, v in Py5KeyEvent.__dict__.items():
            if k == k.upper() and action == v:
                action_str = k
                break

        if key == '\uffff':  # py5.CODED
            key = 'CODED'

        return f"Py5KeyEvent(key=" + key + ", action=" + action_str + ")"

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, name):
        raise AttributeError(spelling.error_msg('Py5KeyEvent', name, self))

    ALT = 8
    CTRL = 2
    META = 4
    PRESS = 1
    RELEASE = 2
    SHIFT = 1
    TYPE = 3

    def get_action(self) -> int:
        """Return the key event's action.

        Underlying Processing method: KeyEvent.getAction

        Notes
        -----

        Return the key event's action. This value will always be implied by the
        triggered event function, but perhaps it might be useful to someone someday.
        """
        return self._instance.getAction()

    @_convert_jchar_to_chr
    def get_key(self) -> chr:
        """Return the key for the key event.

        Underlying Processing method: KeyEvent.getKey

        Notes
        -----

        Return the key for the key event. If the value is `CODED`, use
        `Py5KeyEvent.get_key_code()` instead. This information can also be obtained with
        `key`.
        """
        return self._instance.getKey()

    @_convert_jint_to_int
    def get_key_code(self) -> int:
        """Return the key code for the key event.

        Underlying Processing method: KeyEvent.getKeyCode

        Notes
        -----

        Return the key code for the key event. This method is important for key events
        involving coded keys such as the arrow or modifier keys. This information can
        also be obtained with `key_code`.
        """
        return self._instance.getKeyCode()

    def get_millis(self) -> int:
        """Return the event's timestamp.

        Underlying Processing method: KeyEvent.getMillis

        Notes
        -----

        Return the event's timestamp. This will be measured in milliseconds.
        """
        return self._instance.getMillis()

    def get_modifiers(self) -> int:
        """Integer value used to identify which modifier keys (if any) are currently
        pressed.

        Underlying Processing method: KeyEvent.getModifiers

        Notes
        -----

        Integer value used to identify which modifier keys (if any) are currently
        pressed. Information about the modifier keys is encoded in the integer value and
        can be parsed with bit masking, as shown in the example.
        """
        return self._instance.getModifiers()

    def get_native(self) -> Any:
        """Retrieve native key event object.

        Underlying Processing method: KeyEvent.getNative

        Notes
        -----

        Retrieve native key event object. The returned object will be a Java object and
        its type can vary based on the renderer used by the Sketch and the operating
        system the Sketch is run on. Sometimes the native object can be used to access
        functionality not otherwise available through Processing or py5.

        Be aware that it is possible for the native event object to be `None`, such as
        when interacting with a Sketch through `py5_tools.sketch_portal()`.
        """
        return self._instance.getNative()

    def is_alt_down(self) -> bool:
        """Return boolean value reflecting if the Alt key is down.

        Underlying Processing method: KeyEvent.isAltDown

        Notes
        -----

        Return boolean value reflecting if the Alt key is down. The Alt key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isAltDown()

    def is_auto_repeat(self) -> bool:
        """Identifies if the pressed key is auto repeating, as faciliated by the computer's
        operating system.

        Underlying Processing method: KeyEvent.isAutoRepeat

        Notes
        -----

        Identifies if the pressed key is auto repeating, as faciliated by the computer's
        operating system. This method might work differently (or not at all) depending
        on the renderer used by the Sketch and the operating system the Sketch is run
        on.
        """
        return self._instance.isAutoRepeat()

    def is_control_down(self) -> bool:
        """Return boolean value reflecting if the Control key is down.

        Underlying Processing method: KeyEvent.isControlDown

        Notes
        -----

        Return boolean value reflecting if the Control key is down. The Control key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isControlDown()

    def is_meta_down(self) -> bool:
        """Return boolean value reflecting if the Meta key is down.

        Underlying Processing method: KeyEvent.isMetaDown

        Notes
        -----

        Return boolean value reflecting if the Meta key is down. The Meta key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isMetaDown()

    def is_shift_down(self) -> bool:
        """Return boolean value reflecting if the Shift key is down.

        Underlying Processing method: KeyEvent.isShiftDown

        Notes
        -----

        Return boolean value reflecting if the Shift key is down. The Shift key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isShiftDown()
