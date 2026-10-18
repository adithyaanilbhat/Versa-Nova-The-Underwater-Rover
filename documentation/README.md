# Documentation — Versa Nova: The Underwater Rover

This directory contains the technical documentation for **Versa Nova: The Underwater Rover**, an underwater robotic system developed for visual inspection of submerged structures, such as dam walls and bridge pillars. The project integrates an operator-controlled propulsion system, underwater imaging, and CNN-based crack classification.

## Documentation Contents

### 1. Working Principle

**File:** `working-principle.md`

Explains the overall operating principle of the rover, including operator control, thruster-based movement, underwater image acquisition, image processing, and CNN-based crack classification.

### 2. Mathematical Analysis

**File:** `mathematics_analysis.md`

Presents the mathematical concepts relevant to the rover, including thruster-force analysis, movement principles, force calculations, and battery-runtime estimation.

### 3. CAD Models

**Folder:** `CAD/`

Contains the mechanical CAD models and related design files developed for the rover.

### 4. Electronic Components

**Folder:** `Electronic components/`

Contains information about the electronic hardware and components used in the project, including the onboard computing unit, flight controller, camera, propulsion components, and power-distribution hardware.

### 5. Rover Block Diagram

**File:** `Rover Block Diagram.png`

Provides a visual representation of the rover's major subsystems and their overall relationships.

## Project Scope

The project focuses on underwater visual inspection and image-based classification of surface cracks. The current CNN model performs binary classification, identifying an image as either **Crack** or **No Crack**.

The rover is operator-controlled. Autonomous navigation and other advanced capabilities may be considered for future development.

## Note

This documentation describes the project's general architecture, operating principles, mathematical concepts, mechanical models, and electronic hardware. Detailed information about potentially patentable design features is intentionally excluded from the public documentation.

