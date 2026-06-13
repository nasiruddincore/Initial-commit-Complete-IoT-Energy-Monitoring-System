// Use the ADC to read the current sensor signal
float getIrms() {
  int sensorValue = analogRead(34);
  // Convert analog reading to current (Amps) based on your sensor calibration
  float current = (sensorValue - 2048) * (3.3 / 4095.0) * calibrationFactor;
  return abs(current);
}