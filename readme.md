# Kivy Android Examples Repository


This is a collection of app templates that I have tested as working on android.

## Installation and Building an APK with Buildozer


To build and deploy an APK using Buildozer, follow these steps:

### 1. Install Dependencies
First, ensure you have Python and pip installed. Then, install the necessary Python packages:

```bash
pip install cython kivy kivymd
```

### 2. Install Buildozer

You need Buildozer to package your Kivy application into an APK and Cython. Install it using pip:

```bash
pip install buildozer cython
```

### 3. Update `buildozer.spec`

If you have existing `buildozer.spec` file, make sure to update them with the dependencies used in your project. Add any necessary libraries or modules to the `requirements` section under `[app]` in your `buildozer.spec` file.

### 4. Build the APK

To build and deploy your APK, use the following command:

```bash
buildozer android deploy run
```

- `deploy` will install the APK on your connected Android device or emulator.
- `run` will start the application on the device or emulator.

### 5. Logcat Filtered for Kivy Projects

```bash
adb logcat |grep python
```

