# Mathematical Analysis

## 1. Thruster Force Analysis

The underwater rover uses eight ApisQueen U2 Mini thrusters arranged to provide directional movement and control.

The thrust produced by an individual thruster is specified as approximately 1.3 kgf, equivalent to 12.75 N.

For thrusters mounted at an angle of 45°, the horizontal force component is calculated using:

$$
F_H = F\cos\theta
$$

Where:

* \(F_H\) = Horizontal component of thrust
* \(F\) = Thrust produced by the thruster
* \(\theta\) = Mounting angle

For a mounting angle of 45°:

$$
F_H = F\cos45^\circ
$$

$$
F_H \approx 0.707F
$$

The effective horizontal thrust depends on the thruster arrangement and the direction in which each thruster operates.

## 2. Six Degrees of Freedom (6-DOF)

The rover's eight-thruster configuration is designed to support six degrees of freedom.

| Motion | Description                          |
| ------ | ------------------------------------ |
| Surge  | Forward and backward movement        |
| Sway   | Sideways movement                    |
| Heave  | Upward and downward movement         |
| Roll   | Rotation about the longitudinal axis |
| Pitch  | Rotation about the lateral axis      |
| Yaw    | Rotation about the vertical axis     |

These movements are achieved through suitable combinations of thruster activation and thrust direction.

## 3. Propulsion and Hydrodynamic Resistance

The net force acting on the rover depends on the propulsion force and the opposing hydrodynamic drag.

$$
F_{\text{net}} = F_{\text{thrust}} - F_{\text{drag}}
$$

According to Newton's Second Law:

$$
F_{\text{net}} = ma
$$

Therefore:

$$
a = \frac{F_{\text{net}}}{m}
$$

Where:

* \(F_{\text{net}}\) = Net force acting on the rover
* \(F_{\text{thrust}}\) = Effective propulsion force
* \(F_{\text{drag}}\) = Hydrodynamic drag force
* \(m\) = Mass of the rover
* \(a\) = Acceleration

Actual performance depends on water resistance, thruster efficiency, and operating conditions.

## 4. Power and Battery Considerations

The rover uses LiPo batteries to supply electrical power to its propulsion and electronic systems. Buck converters regulate voltage for compatible electronic components.

Battery capacity is expressed in ampere-hours (Ah). The theoretical operating time can be estimated using:

$$
t = \frac{C}{I}
$$

Where:

* \(t\) = Operating time in hours
* \(C\) = Battery capacity in ampere-hours
* \(I\) = Average current consumption in amperes

Actual operating time depends on the total electrical load, propulsion demand, battery condition, and conversion losses.

## 5. CNN-Based Crack Classification

The crack-detection system uses a Convolutional Neural Network (CNN) to classify images into two categories: **Crack** and **No Crack**.

The model uses images resized to \(224 \times 224\) pixels and normalized before prediction.

The output is interpreted using a threshold of 0.5:

$$
\text{Classification} =
\begin{cases}
\text{Crack}, & p > 0.5\\
\text{No Crack}, & p \leq 0.5
\end{cases}
$$

Where \(p\) is the model's predicted output.

The classification represents the model's prediction and does not, by itself, establish the physical dimensions or severity of a crack.
