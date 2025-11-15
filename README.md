# AI vs Human Image Detector

A complete solution for detecting AI-generated vs human-created images, featuring a Flutter mobile app with a clean, professional interface and a Python FastAPI backend powered by machine learning.

## 🚀 Features

- 🖼️ **Image Upload**: Select images from device gallery
- 🤖 **AI Detection**: Determine if an image is AI-generated or human-created
- 📊 **Confidence Scoring**: View confidence percentage for predictions
- 🎨 **Modern UI**: Clean, professional interface with Material Design
- ⚡ **Real-time Analysis**: Fast image processing and results
- 🔄 **Cross-platform**: Works on both iOS and Android

## 🏗️ Architecture

- **Frontend**: Flutter mobile app (`ai_image_detection_flutter/`)
- **Backend**: Python FastAPI server (`server.py`)
- **Model**: `Ateeqq/ai-vs-human-image-detector` from Hugging Face
- **Communication**: REST API with multipart file upload

## 📱 Screenshots

The app features a modern, professional interface with:
- Clean upload interface with visual feedback
- Elegant image display with rounded corners and shadows
- Clear results showing human vs AI detection
- Professional color scheme and typography

## 🛠️ Setup Instructions

### Prerequisites

- Flutter SDK (3.10.0 or higher)
- Python 3.8 or higher
- iOS/Android development environment

### 1. Install Python Dependencies

From the project root directory:

```bash
pip install fastapi uvicorn torch torchvision torchaudio transformers pillow
```

### 2. Get Your Local IP Address

Find your machine's local IP address:

**macOS/Linux:**
```bash
ipconfig getifaddr en0
```

**Windows:**
```bash
ipconfig
```

Example output: `192.168.1.100`

### 3. Start the Backend Server

Run the FastAPI server with your local IP:

```bash
uvicorn server:app --reload --host 192.168.1.100 --port 8000
```

Replace `192.168.1.100` with your actual IP address. Keep this terminal running.

### 4. Configure the Flutter App

Update the endpoint in the Flutter app:

1. Open `ai_image_detection_flutter/lib/main.dart`
2. Find the `_endpoint` variable (around line 71)
3. Update it with your IP address:

```dart
final String _endpoint = 'http://192.168.1.100:8000/classify';
```

### 5. Run the Flutter App

From the `ai_image_detection_flutter/` directory:

```bash
cd ai_image_detection_flutter
flutter pub get
flutter run
```

### 6. Test the Application

1. Open the app on your device
2. Tap "Select Image" to choose an image from your gallery
3. Wait for the analysis to complete
4. View the results showing whether the image is AI-generated or human-created

## 📁 Project Structure

```
ai-vs-human-image-detector/
├── ai_image_detection_flutter/  # Flutter mobile app
│   ├── lib/
│   │   └── main.dart           # Main Flutter application
│   ├── pubspec.yaml            # Flutter dependencies
│   ├── android/                # Android-specific files
│   ├── ios/                    # iOS-specific files
│   └── README.md              # Flutter app documentation
├── server.py                   # FastAPI backend server
└── README.md                  # This file
```

## 🔌 API Documentation

### POST `/classify`

Analyzes an uploaded image to determine if it's AI-generated or human-created.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: Image file (JPEG, PNG supported)

**Response:**
```json
{
  "label": "hum" | "ai",
  "confidence": 0.95,
  "allow": true,
  "scores": {
    "hum": 0.95,
    "ai": 0.05
  }
}
```

**Response Fields:**
- `label`: Classification result ("hum" for human, "ai" for AI-generated)
- `confidence`: Confidence score for the prediction (0.0 to 1.0)
- `allow`: Boolean indicating if image passes threshold (human with ≥90% confidence)
- `scores`: Detailed scores for both classes

## 🔧 Development

### Backend Development

The FastAPI server (`server.py`) handles:
- Image upload and processing
- ML model inference using Hugging Face Transformers
- CORS configuration for mobile app communication
- Error handling and response formatting

### Frontend Development

The Flutter app (`ai_image_detection_flutter/`) features:
- Material Design 3 theming
- Professional color scheme and typography
- Responsive layout with proper spacing
- Error handling and loading states
- Clean architecture with separated UI components

### Adding New Features

1. **Backend Changes**: Modify `server.py`
2. **Frontend Changes**: Update `ai_image_detection_flutter/lib/main.dart`
3. **Dependencies**: 
   - Python: Install via pip
   - Flutter: Add to `ai_image_detection_flutter/pubspec.yaml`

## 🚀 Building for Production

### Android
```bash
cd ai_image_detection_flutter
flutter build apk --release
```

### iOS
```bash
cd ai_image_detection_flutter
flutter build ios --release
```

## 🔍 Troubleshooting

### Common Issues

1. **Connection Error**: 
   - Ensure both devices are on the same network
   - Verify the server is running and accessible
   - Check firewall settings

2. **Model Loading**: 
   - First run may take longer as the AI model downloads
   - Ensure stable internet connection
   - Check available disk space

3. **Image Format**: 
   - Ensure images are in supported formats (JPEG, PNG)
   - Check image file size (large files may timeout)

### Network Configuration

- **iOS Simulator**: Use `http://localhost:8000/classify`
- **Android Emulator**: Use `http://10.0.2.2:8000/classify`
- **Physical Devices**: Use your machine's local IP address

### Performance Tips

- Use images with reasonable resolution (1-5MB recommended)
- Ensure stable network connection for best performance
- Consider implementing image compression for large files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the AI detection model
- [Flutter](https://flutter.dev/) for the mobile framework
- [FastAPI](https://fastapi.tiangolo.com/) for the backend framework
