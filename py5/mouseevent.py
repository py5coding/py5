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

import weakref

from . import spelling


class Py5MouseEvent:
    """Datatype for providing information about mouse events.

    Underlying Processing class: MouseEvent.MouseEvent

    Notes
    -----

    Datatype for providing information about mouse events. An instance of this class
    will be passed to user-defined mouse event functions if py5 detects those
    functions accept 1 (positional) argument, as demonstrated in the example code.
    The mouse event functions can be any of `mouse_clicked()`, `mouse_dragged()`,
    `mouse_moved()`, `mouse_entered()`, `mouse_exited()`, `mouse_pressed()`,
    `mouse_released()`, or `mouse_wheel()`. Mouse events can be generated faster
    than the frame rate of the Sketch, making mouse event functions useful for
    capturing all of a user's mouse activity.
    """
    _py5_object_cache = weakref.WeakSet()

    def __new__(cls, pmouseevent):
        for o in cls._py5_object_cache:
            if pmouseevent == o._instance:
                return o
        else:
            o = object.__new__(Py5MouseEvent)
            o._instance = pmouseevent
            cls._py5_object_cache.add(o)
            return o

    def __str__(self):
        action = self.get_action()
        action_str = 'UNKNOWN'
        for k, v in Py5MouseEvent.__dict__.items():
            if k == k.upper() and action == v:
                action_str = k
                break
        return f"Py5MouseEvent(x=" + str(self.get_x()) + ", y=" + \
            str(self.get_y()) + ", action=" + action_str + ")"

    def __repr__(self):
        return self.__str__()

    def __getattr__(self, name):
        raise AttributeError(spelling.error_msg('Py5MouseEvent', name, self))

    ALT = 8
    CLICK = 3
    CTRL = 2
    DRAG = 4
    ENTER = 6
    EXIT = 7
    META = 4
    MOVE = 5
    PRESS = 1
    RELEASE = 2
    SHIFT = 1
    WHEEL = 8

    def get_action(self) -> int:
        """Return the mouse event's action.

        Underlying Processing method: MouseEvent.getAction

        Notes
        -----

        Return the mouse event's action. This value will always be implied by the
        triggered event function, but perhaps it might be useful to someone someday.
        """
        return self._instance.getAction()

    def get_button(self) -> int:
        """Identify the mouse button used in the event.

        Underlying Processing method: MouseEvent.getButton

        Notes
        -----

        Identify the mouse button used in the event. This can be `LEFT`, `CENTER`, or
        `RIGHT`.
        """
        return self._instance.getButton()

    def get_count(self) -> int:
        """Get the number of mouse clicks.

        Underlying Processing method: MouseEvent.getCount

        Notes
        -----

        Get the number of mouse clicks. This will be 1 for a single mouse click and 2
        for a double click. The value can be much higher if the user clicks fast enough.
        """
        return self._instance.getCount()

    def get_millis(self) -> int:
        """Return the event's timestamp.

        Underlying Processing method: MouseEvent.getMillis

        Notes
        -----

        Return the event's timestamp. This will be measured in milliseconds.
        """
        return self._instance.getMillis()

    def get_modifiers(self) -> int:
        """Integer value used to identify which modifier keys (if any) are currently
        pressed.

        Underlying Processing method: MouseEvent.getModifiers

        Notes
        -----

        Integer value used to identify which modifier keys (if any) are currently
        pressed. Information about the modifier keys is encoded in the integer value and
        can be parsed with bit masking, as shown in the example.
        """
        return self._instance.getModifiers()

    def get_native(self) -> Any:
        """Retrieve native mouse event object.

        Underlying Processing method: MouseEvent.getNative

        Notes
        -----

        Retrieve native mouse event object. The returned object will be a Java object
        and its type can vary based on the renderer used by the Sketch and the operating
        system the Sketch is run on. Sometimes the native object can be used to access
        functionality not otherwise available through Processing or py5.

        Be aware that it is possible for the native event object to be `None`, such as
        when interacting with a Sketch through `py5_tools.sketch_portal()`.
        """
        return self._instance.getNative()

    def get_x(self) -> int:
        """Return the x position of the mouse at the time of this mouse event.

        Underlying Processing method: MouseEvent.getX

        Notes
        -----

        Return the x position of the mouse at the time of this mouse event. This
        information can also be obtained with `mouse_x`.
        """
        return self._instance.getX()

    def get_y(self) -> int:
        """Return the y position of the mouse at the time of this mouse event.

        Underlying Processing method: MouseEvent.getY

        Notes
        -----

        Return the y position of the mouse at the time of this mouse event. This
        information can also be obtained with `mouse_y`.
        """
        return self._instance.getY()

    def is_alt_down(self) -> bool:
        """Return boolean value reflecting if the Alt key is down.

        Underlying Processing method: MouseEvent.isAltDown

        Notes
        -----

        Return boolean value reflecting if the Alt key is down. The Alt key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isAltDown()

    def is_control_down(self) -> bool:
        """Return boolean value reflecting if the Control key is down.

        Underlying Processing method: MouseEvent.isControlDown

        Notes
        -----

        Return boolean value reflecting if the Control key is down. The Control key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isControlDown()

    def is_meta_down(self) -> bool:
        """Return boolean value reflecting if the Meta key is down.

        Underlying Processing method: MouseEvent.isMetaDown

        Notes
        -----

        Return boolean value reflecting if the Meta key is down. The Meta key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isMetaDown()

    def is_shift_down(self) -> bool:
        """Return boolean value reflecting if the Shift key is down.

        Underlying Processing method: MouseEvent.isShiftDown

        Notes
        -----

        Return boolean value reflecting if the Shift key is down. The Shift key is a
        modifier key and can be pressed at the same time as other keys.
        """
        return self._instance.isShiftDown()
