import QtQuick 2.15
import QtQuick.Scene3D 2.15
import Qt3D.Core 2.15
import Qt3D.Render 2.15
import Qt3D.Input 2.15
import Qt3D.Extras 2.15

Entity {
    id: root
    property var vertices: []

    Mesh {
        id: mesh
        vertices: vertices
    }

    PhongMaterial {
        id: material
    }

    components: [mesh, material]
}