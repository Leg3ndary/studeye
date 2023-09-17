import time

import adhawkapi
import adhawkapi.frontend
import numpy as np


class FrontendData:
    """BLE Frontend"""

    pos = (0, 0, 0, 0)

    def __init__(self):
        # Instantiate an API object
        # TODO: Update the device name to match your device
        self.api = adhawkapi.frontend.FrontendApi(ble_device_name="ADHAWK MINDLINK-288")

        # Tell the api that we wish to receive eye tracking data stream
        # with self._handle_et_data as the handler
        # self.api.register_stream_handler(adhawkapi.PacketType.EYETRACKING_STREAM, self._handle_et_data)
        self.api.register_stream_handler(
            adhawkapi.PacketType.GAZE, self._handle_et_data
        )
        self.api.set_stream_control(adhawkapi.PacketType.GAZE, 200)


        # Tell the api that we wish to tap into the EVENTS stream
        # with self._handle_events as the handler
        self.api.register_stream_handler(
            adhawkapi.PacketType.EVENTS, self._handle_events
        )

        # Start the api and set its connection callback to self._handle_tracker_connect/disconnect.
        # When the api detects a connection to a MindLink, this function will be run.
        self.api.start(
            tracker_connect_cb=self._handle_tracker_connect,
            tracker_disconnect_cb=self._handle_tracker_disconnect,
        )

    def shutdown(self):
        """Shutdown the api and terminate the bluetooth connection"""
        self.api.shutdown()

    @staticmethod
    def _handle_et_data(et_data: adhawkapi.EyeTrackingStreamData):
        """Handles the latest et data"""
        if et_data.gaze is not None:
            xvec, yvec, zvec, vergence = et_data.gaze
            self.pos = et_data.gaze
            print(f"Gaze={xvec:.2f},y={yvec:.2f},z={zvec:.2f},vergence={vergence:.2f}")

        if et_data.gaze_in_screen is not None:
            xvec, yvec, zvec, vergence = et_data.gaze_in_screen
            print(
                f"Gaze in screen={xvec:.2f},y={yvec:.2f},z={zvec:.2f},vergence={vergence:.2f}"
            )

        if et_data.eye_center is not None:
            if et_data.eye_mask == adhawkapi.EyeMask.BINOCULAR:
                rxvec, ryvec, rzvec, lxvec, lyvec, lzvec = et_data.eye_center
                print(
                    f"Eye center: Left=(x={lxvec:.2f},y={lyvec:.2f},z={lzvec:.2f}) "
                    f"Right=(x={rxvec:.2f},y={ryvec:.2f},z={rzvec:.2f})"
                )

        if et_data.pupil_diameter is not None:
            if et_data.eye_mask == adhawkapi.EyeMask.BINOCULAR:
                rdiameter, ldiameter = et_data.pupil_diameter
                print(f"Pupil diameter: Left={ldiameter:.2f} Right={rdiameter:.2f}")

        if et_data.imu_quaternion is not None:
            if et_data.eye_mask == adhawkapi.EyeMask.BINOCULAR:
                x, y, z, w = et_data.imu_quaternion
                print(f"IMU: x={x:.2f},y={y:.2f},z={z:.2f},w={w:.2f}")

    @staticmethod
    def _handle_events(event_type, timestamp, *args):
        if event_type == adhawkapi.Events.BLINK:
            duration = args[0]
            print(f"Got blink: {timestamp} {duration}")
        if event_type == adhawkapi.Events.EYE_CLOSED:
            eye_idx = args[0]
            print(f"Eye Close: {timestamp} {eye_idx}")
        if event_type == adhawkapi.Events.EYE_OPENED:
            eye_idx = args[0]
            print(f"Eye Open: {timestamp} {eye_idx}")

    def _handle_tracker_connect(self):
        print("Tracker connected")
        self.api.set_et_stream_rate(60, callback=lambda *args: None)

        self.api.set_et_stream_control(
            [
                adhawkapi.EyeTrackingStreamTypes.GAZE,
                adhawkapi.EyeTrackingStreamTypes.EYE_CENTER,
                adhawkapi.EyeTrackingStreamTypes.PUPIL_DIAMETER,
                adhawkapi.EyeTrackingStreamTypes.IMU_QUATERNION,
            ],
            True,
            callback=lambda *args: None,
        )

        self.api.set_event_control(
            adhawkapi.EventControlBit.BLINK, 1, callback=lambda *args: None
        )
        self.api.set_event_control(
            adhawkapi.EventControlBit.EYE_CLOSE_OPEN, 1, callback=lambda *args: None
        )

    def _handle_tracker_disconnect(self):
        print("Tracker disconnected")


def main():
    """App entrypoint"""
    frontend = FrontendData()
    try:
        while True:
            time.sleep(1)

            # def grid_points(
            #     nrows, ncols, xrange=20, yrange=12.5, xoffset=0, yoffset=2.5
            # ):
            #     """Generates a grid of points based on range and number of rows/cols"""
            #     zpos = -0.6  # typically 60cm to screen
            #     # calculate x and y range for a xrange x yrange degree calibration window
            #     xmin, xmax = np.tan(
            #         np.deg2rad([xoffset - xrange, xoffset + xrange])
            #     ) * np.abs(zpos)
            #     ymin, ymax = np.tan(
            #         np.deg2rad([yoffset - yrange, yoffset + yrange])
            #     ) * np.abs(zpos)

            #     cal_points = []
            #     for ypos in np.linspace(ymin, ymax, nrows):
            #         for xpos in np.linspace(xmin, xmax, ncols):
            #             cal_points.append((xpos, ypos, zpos))

            #     print(
            #         f"grid_points(): generated {nrows}x{ncols} points"
            #         f" {xrange}x{yrange} deg box at {zpos}: {cal_points}"
            #     )

            #     return cal_points

            # npoints = 9
            # nrows = int(np.sqrt(npoints))
            # reference_points = grid_points(nrows, nrows)

            # frontend.api.start_calibration()
            # for point in reference_points:
            #     # As the eye moves and fixates on each point on the screen,
            #     # register the position of the point
            #     frontend.api.register_calibration_point(*point)
            # frontend.api.stop_calibration()

    except (KeyboardInterrupt, SystemExit):
        frontend.shutdown()


if __name__ == "__main__":
    main()
