import airsim
from AirSimClient import *

class CarClientForRL(CarClient):
    

    def __init__(self):
        CarClient.__init__(self)
        CarClient.confirmConnection(self)
        self.enableApiControl(True)

    def _take_car_action(self, throttle, steering):
        car_controls = CarControls()
        car_controls.throttle = throttle
        car_controls.steering = steering
        self.setCarControls(car_controls)
        time.sleep(1)

    def _break_car(self):
        # apply breaks
        car_controls = CarControls()
        car_controls.brake = 1
        self.setCarControls(car_controls)
        print("Apply break")
        time.sleep(1)   # let car drive a bit
        car_controls.brake = 0 #remove break
        
    def _reset_car(self):
        #restore to original state
        self.reset()
        self.enableApiControl(False)
    # get camera images from the car
    """responses = client.simGetImages([
        ImageRequest(0, AirSimImageType.DepthVis),  #depth visualiztion image
        ImageRequest(1, AirSimImageType.DepthPerspective, True), #depth in perspective projection
        ImageRequest(1, AirSimImageType.Scene), #scene vision image in png format
        ImageRequest(1, AirSimImageType.Scene, False, False)])  #scene vision image in uncompressed RGBA array
    print('Retrieved images: %d', len(responses))
    
    for response in responses:
        filename = 'c:/temp/py' + str(idx)

        if response.pixels_as_float:
            print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
            AirSimClientBase.write_pfm(os.path.normpath(filename + '.pfm'), AirSimClientBase.getPfmArray(response))
        elif response.compress: #png format
            print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
            AirSimClientBase.write_file(os.path.normpath(filename + '.png'), response.image_data_uint8)
        else: #uncompressed array
            print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
            img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8) #get numpy array
            img_rgba = img1d.reshape(response.height, response.width, 4) #reshape array to 4 channel image array H X W X 4
            img_rgba = np.flipud(img_rgba) #original image is fliped vertically
            img_rgba[:,:,1:2] = 100 #just for fun add little bit of green in all pixels
            AirSimClientBase.write_png(os.path.normpath(filename + '.greener.png'), img_rgba) #write to png """




            
