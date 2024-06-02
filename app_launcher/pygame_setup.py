import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from PyQt5.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *
from pygltflib import GLTF2

class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)
        self.gltf = None
        self.angle = 0
        self.vertices = None
        self.indices = None

    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        
        # Load the .glb model
        self.gltf = GLTF2().load('app_launcher/obj_files/model3d1_test.glb')
        self.load_model()

def load_model(self): #! Issues Here
    try:
        if self.gltf is not None:
            mesh = self.gltf.meshes[0]
            primitive = mesh.primitives[0]

            # Load vertex data
            position_accessor_index = primitive.attributes.get('POSITION', None)
            if position_accessor_index is not None:
                accessor = self.gltf.accessors[position_accessor_index]
                buffer_view = self.gltf.bufferViews[accessor.bufferView]
                buffer = self.gltf.buffers[buffer_view.buffer]
                byte_offset = buffer_view.byteOffset + accessor.byteOffset
                vertex_data = np.frombuffer(buffer.data[byte_offset:byte_offset + accessor.count * 3 * 4], dtype=np.float32)
                self.vertices = vertex_data.reshape((accessor.count, 3))

            # Load index data
            index_accessor_index = primitive.indices
            if index_accessor_index is not None:
                accessor = self.gltf.accessors[index_accessor_index]
                buffer_view = self.gltf.bufferViews[accessor.bufferView]
                buffer = self.gltf.buffers[buffer_view.buffer]
                byte_offset = buffer_view.byteOffset + accessor.byteOffset
                index_data = np.frombuffer(buffer.data[byte_offset:byte_offset + accessor.count * 2], dtype=np.uint16)
                self.indices = index_data
    except Exception as e:
        print("Error loading model:", e)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45.0, w / float(h), 1.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
        
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        
        if self.vertices is not None and self.indices is not None:
            glBegin(GL_TRIANGLES)
            for index in self.indices:
                vertex = self.vertices[index]
                glVertex3f(*vertex)
            glEnd()
        
        self.angle += 1
        self.update()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("3D Game Interface with GLB Model")
        self.setGeometry(100, 100, 800, 600)
        
        self.glWidget = GLWidget(self)
        self.setCentralWidget(self.glWidget)
        
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(16)  # ~60 FPS

    def update(self):
        self.glWidget.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())