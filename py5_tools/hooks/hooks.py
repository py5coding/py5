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
import time


class BaseHook:

    def __init__(self, hook_name):
        self.hook_name = hook_name
        self.is_ready = False
        self.exception = None
        self.is_terminated = False

    def hook_finished(self, sketch):
        sketch._remove_post_hook('draw', self.hook_name)
        self.is_ready = True

    def hook_error(self, sketch, e):
        self.exception = e
        sketch._remove_post_hook('draw', self.hook_name)
        self.is_terminated = True

    def sketch_terminated(self):
        self.is_terminated = True


class ScreenshotHook(BaseHook):

    def __init__(self, filename):
        super().__init__('py5screenshot_hook')
        self.filename = filename

    def __call__(self, sketch):
        try:
            sketch.save_frame(self.filename, use_thread=False)
            self.hook_finished(sketch)
        except Exception as e:
            self.hook_error(sketch, e)


class SaveFramesHook(BaseHook):

    def __init__(self, dirname, filename, period, start, limit):
        super().__init__('py5save_frames_hook')
        self.dirname = dirname
        self.filename = filename
        self.period = period
        self.start = start
        self.limit = limit
        self.num_offset = None
        self.filenames = []
        self.last_frame_time = 0

    def __call__(self, sketch):
        try:
            if time.time() - self.last_frame_time < self.period:
                return
            if self.num_offset is None:
                self.num_offset = 0 if self.start is None else sketch.frame_count - self.start
            num = sketch.frame_count - self.num_offset
            frame_filename = sketch._insert_frame(
                str(self.dirname / self.filename), num=num)
            sketch.save_frame(frame_filename)
            self.filenames.append(frame_filename)
            self.last_frame_time = time.time()
            if len(self.filenames) == self.limit:
                self.hook_finished(sketch)
        except Exception as e:
            self.hook_error(sketch, e)


class GrabFramesHook(BaseHook):

    def __init__(self, period, count):
        super().__init__('py5grab_frames_hook')
        self.period = period
        self.count = count
        self.frames = []
        self.last_frame_time = 0

    def __call__(self, sketch):
        try:
            if time.time() - self.last_frame_time < self.period:
                return
            sketch.load_np_pixels()
            self.frames.append(sketch.np_pixels[:, :, 1:].copy())
            self.last_frame_time = time.time()
            if len(self.frames) == self.count:
                self.hook_finished(sketch)
        except Exception as e:
            self.hook_error(sketch, e)


class SketchPortalHook(BaseHook):
    def __init__(self, displayer, throttle_frame_rate, time_limit):
        super().__init__('py5sketch_portal_hook')
        self.displayer = displayer
        self.period = 1 / throttle_frame_rate if throttle_frame_rate else 0
        self.time_limit = time_limit
        self.last_frame_time = 0
        self.start_time = time.time()

    def __call__(self, sketch):
        try:
            if self.time_limit and time.time() > self.start_time + self.time_limit:
                self.hook_finished(sketch)
            if time.time() < self.last_frame_time + self.period:
                return
            sketch.load_np_pixels()
            self.displayer(sketch.np_pixels[:, :, 1:])
            self.last_frame_time = time.time()
        except Exception as e:
            self.hook_error(sketch, e)
