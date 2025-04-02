/* Simulator for Entangled Photon Measurements */
import 'dart:math';

class EntangledPhotonMeasurement {
  String formatNumber(double value) {
    return value.toStringAsFixed(2);
  }
  
  double square(double value) {
    return value * value;
  }
  
  // State of the photons
  double p00, p01, p10, p11;
  
  EntangledPhotonMeasurement(double i00, double i01, double i10, double i11)
      : p00 = i00, p01 = i01, p10 = i10, p11 = i11 {
    double check = p00*p00 + p01*p01 + p10*p10 + p11*p11;
    if (check > 1.01 || check < 0.99) {
      print("Error: Probabilities must add up to 1");
    }
  }
  
  void setIndependentPhotonAngles(double angle1, double angle2) {
    double r1 = angle1 * pi / 180;
    double r2 = angle2 * pi / 180;
    p00 = cos(r1) * cos(r2);
    p01 = cos(r1) * sin(r2);
    p10 = sin(r1) * cos(r2);
    p11 = sin(r1) * sin(r2);
  }
  
  double m00 = 0, m01 = 0, m10 = 0, m11 = 0, m1angle = 0, m2angle = 0;
  
  void setMeasurementAngles(double angle1, double angle2) {
    m1angle = angle1;
    m2angle = angle2;
    double r1 = angle1 * pi / 180;
    double r2 = angle2 * pi / 180;
    m00 = cos(r1) * cos(r2);
    m01 = cos(r1) * sin(r2);
    m10 = sin(r1) * cos(r2);
    m11 = sin(r1) * sin(r2);
  }
  
  void reportMeasurementProbability() {
    // 11
    double originalp1angle = m1angle;
    double originalp2angle = m2angle;
    double prob11 = square((p00*m00) + (p01*m01) + (p10*m10) + (p11*m11));
    // 01
    setMeasurementAngles(90 + originalp1angle, originalp2angle);
    double prob01 = square((p00*m00) + (p01*m01) + (p10*m10) + (p11*m11));
    // 10
    setMeasurementAngles(originalp1angle, originalp2angle+90);
    double prob10 = square((p00*m00) + (p01*m01) + (p10*m10) + (p11*m11));
    // 00
    setMeasurementAngles(90 + originalp1angle, 90 + originalp2angle);
    double prob00 = square((p00*m00) + (p01*m01) + (p10*m10) + (p11*m11));
    // reset
    setMeasurementAngles(originalp1angle, originalp2angle); // reset to original
    
    print("Probability of 00 = ${formatNumber(prob00)}");
    print("Probability of 01 = ${formatNumber(prob01)}");
    print("Probability of 10 = ${formatNumber(prob10)}");
    print("Probability of 11 = ${formatNumber(prob11)}");

    double tooSmall = 0.00001;
    if (prob01 + prob11 > tooSmall) {
      print("Probability of Photon1 measured to be 1, given that Photon2 was measured to be 1 = ${formatNumber(prob11/(prob01+prob11))}");
    }
    if (prob10 + prob00 > tooSmall) {
      print("Probability of Photon1 measured to be 1, given that Photon2 was measured to be 0 = ${formatNumber(prob10/(prob10+prob00))}");
    }
    if (prob01 + prob11 > tooSmall) {
      print("Probability of Photon1 measured to be 0, given that Photon2 was measured to be 1 = ${formatNumber(prob01/(prob01+prob11))}");
    }
    if (prob10 + prob00 > tooSmall) {
      print("Probability of Photon1 measured to be 0, given that Photon2 was measured to be 0 = ${formatNumber(prob00/(prob10+prob00))}");
    }

    if (prob10 + prob11 > tooSmall) {
      print("Probability of Photon2 measured to be 1, given that Photon1 was measured to be 1 = ${formatNumber(prob11/(prob10+prob11))}");
    }
    if (prob01 + prob00 > tooSmall) {
      print("Probability of Photon2 measured to be 1, given that Photon1 was measured to be 0 = ${formatNumber(prob01/(prob01+prob00))}");
    }
    if (prob10 + prob11 > tooSmall) {
      print("Probability of Photon2 measured to be 0, given that Photon1 was measured to be 1 = ${formatNumber(prob10/(prob10+prob11))}");
    }
    if (prob01 + prob00 > tooSmall) {
      print("Probability of Photon2 measured to be 0, given that Photon1 was measured to be 0 = ${formatNumber(prob00/(prob01+prob00))}");
    }
  }
  
  void performMeasurement() {
    // 11
    double originalp1angle = m1angle;
    double originalp2angle = m2angle;
    setMeasurementAngles(90 + originalp1angle, originalp2angle); // 01
    double prob01 = square((p00*m00) + (p01*m01) + (p10*m10) + (p11*m11));
    setMeasurementAngles(originalp1angle, originalp2angle+90); // 10
    double prob10 = square((p00*m00) + (p01*m01) + (p10*m10) + (p11*m11));
    setMeasurementAngles(90 + originalp1angle, 90+ originalp2angle); // 00
    double prob00 = square((p00*m00) + (p01*m01) + (p10*m10) + (p11*m11));
    // reset
    setMeasurementAngles(originalp1angle, originalp2angle); // reset to original
    
    double rand = Random().nextDouble();
    if (rand < prob00) {
      // Measured to be 00
      double angle1 = m1angle + 90; // Add 90 for anti-alignment. 0 means anti-alignment
      double angle2 = m2angle + 90; // Add 90 for anti-alignment. 0 means anti-alignment
      setIndependentPhotonAngles(angle1, angle2);
      print("-------------------------------------------------------");
      print("Measured 00");
      print("After measurement, the photon angles are ${formatNumber(angle1)} and ${formatNumber(angle2)} and the photon state is ${formatNumber(p00)} ${formatNumber(p01)} ${formatNumber(p10)} ${formatNumber(p11)}");
    } else if (rand < prob00 + prob01) {
      // Measured to be 01
      double angle1 = m1angle + 90; // Add 90 for anti-alignment. 0 means anti-alignment
      double angle2 = m2angle; // 1 means alignment. Don't add 90
      setIndependentPhotonAngles(angle1, angle2);
      print("-------------------------------------------------------");
      print("Measured 01");
      print("After measurement, the photon angles are ${formatNumber(angle1)} and ${formatNumber(angle2)} and the photon state is ${formatNumber(p00)} ${formatNumber(p01)} ${formatNumber(p10)} ${formatNumber(p11)}");
    } else if (rand < prob00 + prob01 + prob10) {
      // Measured to be 10
      double angle1 = m1angle; // 1 means alignment. Don't add 90
      double angle2 = m2angle + 90; // Add 90 for anti-alignment. 0 means anti-alignment
      setIndependentPhotonAngles(angle1, angle2);
      print("-------------------------------------------------------");
      print("Measured 10");
      print("After measurement, the photon angles are ${formatNumber(angle1)} and ${formatNumber(angle2)} and the photon state is ${formatNumber(p00)} ${formatNumber(p01)} ${formatNumber(p10)} ${formatNumber(p11)}");
    } else {
      // Measured to be 11
      double angle1 = m1angle; // 1 means alignment. Don't add 90
      double angle2 = m2angle; // 1 means alignment. Don't add 90
      setIndependentPhotonAngles(angle1, angle2);
      print("-------------------------------------------------------");
      print("Measured 11");
      print("After measurement, the photon angles are ${formatNumber(angle1)} and ${formatNumber(angle2)} and the photon state is ${formatNumber(p00)} ${formatNumber(p01)} ${formatNumber(p10)} ${formatNumber(p11)}");
    }
  }
  
  static void run() {
    // Compute probabilities. But we don't make any measurement. So the Photon state is not changed.
    // EntangledPhotonMeasurement pairPrediction = EntangledPhotonMeasurement(0.707106, 0, 0, 0.707106); // Square root of 1/2, probabilities of entangled photon states
    EntangledPhotonMeasurement pairPrediction = EntangledPhotonMeasurement( 0, 0.707106, -0.707106, 0); // square is 1/2 probability, complex number
    pairPrediction.setMeasurementAngles(90, 90); //aligned apparatus, one apparatus per photon
      // Probability of 00 = 0.50
      // Probability of 01 = 0.00
      // Probability of 10 = 0.00
      // Probability of 11 = 0.50
    // pairPrediction.setMeasurementAngles(10, 90); // non-aligned apparatus, changes the probabilites
      // Probability of 00 = 0.02
      // Probability of 01 = 0.48
      // Probability of 10 = 0.48
      // Probability of 11 = 0.02
    pairPrediction.reportMeasurementProbability();
    
    // Perform some measurements. Measurements will change the photon states.
    for(int i = 0; i < 100; i++) {
      EntangledPhotonMeasurement pairExperiment = EntangledPhotonMeasurement(0.707106, 0, 0, 0.707106);
      // pairExperiment.setMeasurementAngles(90, 90);
      pairExperiment.setMeasurementAngles(10, 80);
      pairExperiment.performMeasurement();
    }
  }
}

void main() {
  EntangledPhotonMeasurement.run();
}
