''' Demonstrates how to subscribe to and handle data from gaze and event streams '''

import time
import keyboard

import adhawkapi
import adhawkapi.frontend

pos = None

class FrontendData:
    ''' BLE Frontend '''

    def __init__(self):
        # Instantiate an API object
        # TODO: Update the device name to match your device
        self._api = adhawkapi.frontend.FrontendApi(ble_device_name='ADHAWK MINDLINK-288')

        # Tell the api that we wish to receive eye tracking data stream
        # with self._handle_et_data as the handler
        self._api.register_stream_handler(adhawkapi.PacketType.EYETRACKING_STREAM, self._handle_et_data)

        # Tell the api that we wish to tap into the EVENTS stream
        # with self._handle_events as the handler
        #self._api.register_stream_handler(adhawkapi.PacketType.EVENTS, self._handle_events)

        # Start the api and set its connection callback to self._handle_tracker_connect/disconnect.
        # When the api detects a connection to a MindLink, this function will be run.
        self._api.start(tracker_connect_cb=self._handle_tracker_connect,
                        tracker_disconnect_cb=self._handle_tracker_disconnect)

    def shutdown(self):
        '''Shutdown the api and terminate the bluetooth connection'''
        self._api.shutdown()

    @staticmethod
    def _handle_et_data(et_data: adhawkapi.EyeTrackingStreamData):
        ''' Handles the latest et data '''
        '''
        if et_data.gaze is not None and keyboard.is_pressed("r"):
            xvec, yvec, zvec, vergence = et_data.gaze
            print(f'Gaze={xvec:.2f},y={yvec:.2f},z={zvec:.2f},vergence={vergence:.2f}')
            while keyboard.is_pressed('r'):
                pass
        '''
        global pos
        if et_data.gaze is not None:
            pos = et_data.gaze
        else:
            pos = None
        
    def _handle_tracker_connect(self):
        print("Tracker connected")
        self._api.set_et_stream_rate(60, callback=lambda *args: None)

        self._api.set_et_stream_control([
            adhawkapi.EyeTrackingStreamTypes.GAZE,
            adhawkapi.EyeTrackingStreamTypes.EYE_CENTER,
            adhawkapi.EyeTrackingStreamTypes.PUPIL_DIAMETER,
            adhawkapi.EyeTrackingStreamTypes.IMU_QUATERNION,
        ], True, callback=lambda *args: None)

        self._api.set_event_control(adhawkapi.EventControlBit.BLINK, 1, callback=lambda *args: None)
        self._api.set_event_control(adhawkapi.EventControlBit.EYE_CLOSE_OPEN, 1, callback=lambda *args: None)

    def _handle_tracker_disconnect(self):
        print("Tracker disconnected")

def main():
    global pos
    ''' App entrypoint '''
    frontend = FrontendData()
    
    try:
        while True:
            time.sleep(1)
            if keyboard.is_pressed("r"):
                xvec, yvec, zvec, vergence = pos
                print(f'Gaze={xvec:.2f},y={yvec:.2f},z={zvec:.2f},vergence={vergence:.2f}')
                while keyboard.is_pressed('r'):
                    pass
    except (KeyboardInterrupt, SystemExit):
        frontend.shutdown()

if __name__ == '__main__':
    main()
