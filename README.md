# 🌊 Versa Nova: The Underwater Rover

An underwater robotic system developed for structural inspection, visual monitoring, and CNN-based crack detection.

## 📌 Overview

**Versa Nova** is a final-year project developed as part of the B.Tech in Robotics and Automation at Adi Shankara Institute of Engineering and Technology, Kalady.

The project focuses on underwater inspection of structures such as dam walls and bridge pillars. It combines a multi-thruster propulsion system, onboard computing, camera-based monitoring, buoyancy management, and deep-learning-based image classification.

## ✨ Key Features

* **Multidirectional Propulsion:** Eight-thruster configuration designed to support movement along multiple axes.
* **Buoyancy Management:** An integrated system designed to support controlled vertical movement underwater.
* **Visual Monitoring:** Camera-based observation of submerged structures.
* **CNN-Based Crack Detection:** Image classification into *Crack* and *No Crack* categories.
* **Embedded Computing:** Raspberry Pi 5 for onboard processing.
* **Vehicle Control:** Pixhawk 2.4.8 integrated into the control architecture.
* **Tethered Communication:** Ethernet-based communication with the surface-side system.

## 🔧 Hardware

* Raspberry Pi 5 (8 GB RAM)
* Pixhawk 2.4.8
* 8 × ApisQueen U2 Mini thrusters
* USB camera
* Buoyancy tanks and pumping components
* RadioMaster Pocket controller
* LiPo batteries
* Buck converters
* Ethernet tether
* Protective electronics enclosure

## 💻 Software and Technologies

* Python
* Convolutional Neural Networks (CNN)
* Image preprocessing and classification
* Embedded systems
* Underwater robotics
* Vehicle control systems

*The specific software libraries, versions, and execution instructions will be documented alongside the implementation files.*

## 🧠 Crack Detection

The project incorporates a CNN-based image classification system to identify images that may contain visible cracks.

The processing pipeline includes:

1. Image acquisition.
2. Image resizing to 224 × 224 pixels.
3. Image normalisation.
4. CNN-based feature extraction and classification.
5. Probability-based classification into Crack or No Crack.

The model is intended to support preliminary visual inspection. Its predictions do not independently establish crack dimensions, severity, or structural integrity.

## 🏗️ Potential Applications

* Dam wall inspection
* Bridge pillar monitoring
* Underwater structural surveillance
* Research in underwater robotics and computer vision

## 🚀 Future Development

Potential enhancements include autonomous navigation, sonar integration, improved underwater sensing, and advanced crack localisation and measurement.

These are proposed future developments and should not be interpreted as existing capabilities.

## 👥 Project Team

* Adithya Anil Bhat
* Dino Davis
* Karthik Biju
* Nandana K D

**Project Guide:** Dr. Sreedeep Krishnan
**Department:** Robotics and Automation
**Institution:** Adi Shankara Institute of Engineering and Technology, Kalady
**University:** APJ Abdul Kalam Technological University (KTU)
**Academic Year:** 2025–2026

## 📌 Project Status

The project integrates underwater robotics hardware with buoyancy management and CNN-based crack image classification. Further development and testing can expand its inspection capabilities.

---

*Versa Nova explores the integration of robotics, embedded systems, and computer vision for underwater inspection.*
