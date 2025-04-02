/* Simulator for Photon Qubit Measurements */
import 'dart:math';

class PhotonPolarizationMeasurement {
  double polarizationAngle;

  PhotonPolarizationMeasurement(double angle) : polarizationAngle = angle;
  
  // Measurement returns boolean true for "aligned" and false for "anti-aligned"
  // Qubit value 1 = Aligned (true)
  // Qubit value 0 = Anti-Aligned (false)
  // Observe how measurement causes the state to change
  bool measurePolarization(double angle) {
    double diffAngle = angle - polarizationAngle;
    double cosDiffAngle = cos(diffAngle * pi / 180);
    double probabilityAlign = cosDiffAngle * cosDiffAngle;
    
    if (Random().nextDouble() < probabilityAlign) {
      polarizationAngle = angle;
      return true; // TRUE means "Aligned"
    } else {
      polarizationAngle = angle + 90;
      return false; // FALSE means "Anti-Aligned"
    }
  }
  
  static void main() {

    // List of angle pairs to test (initial angle, measurement angle)
    List<List<double>> anglePairs = [
      [0, 90],
      [0, 0],
      [0, 70],
      [0, 45],
      [45, 135], 
      [60, 30],
      [90, 0],
      [120, 60],
      [135, 45],
      [150, 90],
      [180, 135],
      [210, 45]
    ];

    // Run 1000 tests for each angle pair
    for (var angles in anglePairs) {
      int trueCount = 0;
      int falseCount = 0;
      
      for (int i = 0; i < 1000; i++) {
        PhotonPolarizationMeasurement photon = PhotonPolarizationMeasurement(angles[0]);
        if (photon.measurePolarization(angles[1])) {
          trueCount++;
        } else {
          falseCount++;
        }
      }

      // Calculate statistics
      double mean = (1.0 * trueCount + 0 * falseCount) / (trueCount + falseCount);
      double variance = ((1.0 - mean) * (1.0 - mean) * trueCount + mean * mean * falseCount) / (trueCount + falseCount);
      double sd = sqrt(variance);

      print("\nInitial angle: ${angles[0]}°, Measurement angle: ${angles[1]}°");
      print("MEAN: $mean");
      print("Standard Deviation: $sd");
    }
  }
} 