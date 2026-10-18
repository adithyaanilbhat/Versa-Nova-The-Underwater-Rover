# Working Principle — Versa Nova: The Underwater Rover

## 1. Introduction

Versa Nova: The Underwater Rover is an underwater robotic system developed for visual inspection and monitoring of submerged structures, particularly dam walls and bridge pillars. The system integrates an eight-thruster propulsion arrangement, a flight controller, an onboard processing unit, an underwater camera, and a CNN-based crack-classification system.

The rover combines mechanical, electronic, and software components to support underwater movement and image-based inspection of submerged surfaces.

## 2. System Architecture

The major subsystems of Versa Nova are:

* **Propulsion system:** Eight ApisQueen U2 Mini thrusters support multidirectional movement.
* **Motion-control system:** A Pixhawk 2.4.8 flight controller manages vehicle motion according to the implemented configuration.
* **Processing system:** A Raspberry Pi 5 with 8 GB RAM provides the onboard computing platform.
* **Imaging system:** A USB camera captures images of underwater surfaces.
* **Crack-classification system:** A Convolutional Neural Network (CNN) classifies images into crack and no-crack categories.
* **Power system:** LiPo batteries supply electrical power, while buck converters regulate voltage for electronic components.
* **Communication system:** An Ethernet cable provides a communication link between the rover and the surface-side system.

These subsystems work together to support underwater movement, visual observation, and image-based crack classification.

## 3. Operator Control and Motion Management

The rover incorporates a RadioMaster Pocket controller for operator input and a Pixhawk 2.4.8 flight controller for vehicle motion control.

The operator provides movement commands through the control arrangement. The flight controller manages vehicle motion according to the implemented configuration, while the propulsion system produces the thrust required to move the rover through the water.

The system is designed to support movement in multiple directions and assist with positioning near underwater surfaces for inspection.

The rover is operator-controlled; autonomous navigation is not presented as an implemented capability.

## 4. Eight-Thruster Propulsion System

The propulsion system consists of eight ApisQueen U2 Mini thrusters arranged to support multidirectional movement.

The thruster arrangement is intended to support movement along three translational axes and rotation about three axes. These six degrees of freedom are commonly described as:

* **Surge:** Forward and backward movement.
* **Sway:** Sideways movement.
* **Heave:** Upward and downward movement.
* **Roll:** Rotation about the longitudinal axis.
* **Pitch:** Rotation about the lateral axis.
* **Yaw:** Rotation about the vertical axis.

The thrusters generate forces that move or orient the rover according to their arrangement and the control commands.

Actual movement depends on thruster orientation, available thrust, vehicle mass distribution, hydrodynamic resistance, and the implemented control configuration.

## 5. Underwater Imaging

Visual observation is an essential part of the rover's inspection function.

A USB camera connected to the Raspberry Pi 5 captures images of the underwater surroundings. These images provide visual information about submerged surfaces and can be used as input to the crack-classification software.

The captured images are relevant when inspecting surfaces such as dam walls and bridge pillars, where visible cracks may require further examination.

Image quality and usefulness depend on factors such as lighting, water clarity, camera positioning, distance from the inspected surface, and image resolution.

## 6. CNN-Based Crack Classification

The project incorporates a Convolutional Neural Network (CNN) developed using Python and TensorFlow/Keras to classify images into two categories:

1. Crack
2. No Crack

The model is trained using a dataset containing images of cracked and non-cracked surfaces. The images are organised into the corresponding categories so that the model can learn visual features associated with each class.

### 6.1 Image Preprocessing

Before being supplied to the CNN, images are resized to 224 × 224 pixels and their pixel values are normalised.

Standardising image dimensions provides a consistent input format for the model. Normalisation scales the image data for neural-network processing.

### 6.2 Feature Extraction

The CNN uses convolutional layers to learn visual features from the input images. These features may include edges, textures, and patterns associated with cracks.

Max-pooling layers reduce the spatial dimensions of the extracted features while retaining information useful for classification.

The resulting features are passed through flattening and fully connected layers before reaching the final classification stage.

### 6.3 Binary Classification

The final output layer uses a sigmoid activation function to produce a prediction value between 0 and 1.

The implemented classification rule is:

* If the prediction value is greater than 0.5, the image is classified as **Crack**.
* If the prediction value is less than or equal to 0.5, the image is classified as **No Crack**.

The threshold determines which category is assigned to the input image.

The prediction value is a model output used for classification; it should not automatically be interpreted as a verified probability that a physical crack exists.

### 6.4 Model Training

The model uses the Adam optimiser and binary cross-entropy loss function. The dataset is divided into training and validation subsets to support model training and evaluation.

After training, the model is saved and can be loaded by the testing script to classify new images.

The classification output indicates whether the supplied image is assigned to the crack or no-crack category. It does not, by itself, determine the crack's physical dimensions, depth, or severity.

## 7. Power Distribution

Electrical power is supplied by the rover's LiPo battery configuration. Buck converters are incorporated to regulate voltage for electronic components according to their requirements.

The power system supports the processing unit, control electronics, camera, propulsion components, and associated systems.

Actual operating time depends on the connected loads, propulsion demand, battery condition, converter efficiency, and operating conditions. Battery capacity alone does not establish the rover's actual runtime.

## 8. Communication System

An Ethernet cable is incorporated into the rover's communication arrangement to provide a link between the underwater system and the surface-side equipment.

The communication link supports the intended exchange of information between the rover and the operator-side system.

The precise data flow and control-interface implementation depend on the configured hardware and software. The presence of an Ethernet connection alone does not establish that every control signal, camera stream, or CNN result is transmitted through the same channel.

## 9. Overall Operating Sequence

The overall working sequence can be summarised as follows:

1. Power is supplied to the rover's electronic and propulsion systems.
2. The operator provides movement commands through the control arrangement.
3. The Pixhawk flight controller manages vehicle motion according to the implemented configuration.
4. The eight-thruster propulsion system produces the forces required for movement.
5. The USB camera captures images of the underwater surroundings.
6. The Raspberry Pi 5 provides the computing platform for image processing and CNN-based crack classification.
7. The trained CNN processes an input image and assigns it to the crack or no-crack category.
8. The classification output can be examined as part of the visual inspection process.

The exact sequence and timing of operations depend on the deployed software, communication setup, and control implementation.

## 10. Applications

The system is intended to support underwater visual inspection and monitoring, particularly in applications involving:

* Inspection of submerged dam surfaces.
* Visual examination of bridge pillars.
* Identification of visible cracks in underwater images.
* Underwater surveillance and observation.
* Preliminary image-based assessment of submerged structures.

The CNN classification output can assist inspection, but physical confirmation and further engineering assessment may be necessary before drawing conclusions about a structure's condition.

## 11. Scope and Limitations

The current project focuses on operator-controlled movement, underwater imaging, and binary CNN-based crack classification.

The following distinctions are important:

* Autonomous navigation is a potential future development, not an established current capability.
* The CNN classifies images as crack or no-crack; this description does not claim automatic crack-length or crack-width measurement.
* Image classification does not establish crack depth, structural integrity, or the severity of damage.
* Detection performance depends on the training dataset, image quality, underwater visibility, and the characteristics of the inspected surface.
* Actual movement, communication performance, and operating duration depend on the implemented configuration and verified test results.

## 12. Conclusion

Versa Nova integrates an eight-thruster propulsion system, a Pixhawk 2.4.8 flight controller, Raspberry Pi 5 onboard computing, underwater imaging, and CNN-based image classification.

The propulsion and control systems support underwater movement, while the camera and trained CNN provide a method for classifying captured images into crack and no-crack categories.

By combining these subsystems, the project establishes a platform for underwater visual inspection and image-based crack classification. Further improvements may focus on enhancing image quality, evaluating classification performance, and developing additional inspection capabilities.
