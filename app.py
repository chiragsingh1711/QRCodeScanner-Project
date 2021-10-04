from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import cv2
from pyzbar.pyzbar import decode

class MainApp(App):
    def build(self):
        self.camera_object = Camera()

        # Button Take Pic
        self.button_object = Button(text="Take Pic")
        self.button_object.size_hint = (0.2, 0.2)
        self.button_object.pos_hint = {'x': 0.25, 'y': 0}
        self.button_object.bind(on_press=self.take_pic)

        self.layout_object = BoxLayout()
        self.layout_object.add_widget(self.camera_object)
        self.layout_object.add_widget(self.button_object)
        return self.layout_object


    def take_pic(self, *args):
        print("Pic Done")

        File_name = "IMG.png"
        self.camera_object.export_to_png(File_name)
        img = cv2.imread(File_name)

        detectedBarcodes = decode(img)

        for barcode in detectedBarcodes:
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                # Print the barcode data
                print("https://"+barcode.data.decode("UTF-8"))
                print(barcode.type)

        cv2.imshow("Image", img)
        cv2.waitKey(0)





if __name__ == '__main__':
    app = MainApp()
    app.run()