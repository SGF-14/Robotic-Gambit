import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'splash_screen.dart'; // Assuming SplashScreen is the entry widget of your app

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: FirebaseOptions(
        apiKey: "AIzaSyCptp914bSATMuZUd-5Y_aXgV8e1QpujPM", // Your apiKey
        authDomain: "robotic-gambit.firebaseapp.com", // Your authDomain
        databaseURL: "https://robotic-gambit-default-rtdb.europe-west1.firebasedatabase.app",
        projectId: "robotic-gambit", // Your projectId
        storageBucket: "robotic-gambit.appspot.com", // Your storageBucket
        messagingSenderId: "737950787363", // Your messagingSenderId
        appId: "1:737950787363:web:dd1e840e33e43c5d730e96", // Your appId
        measurementId: "G-X37MLDPFXH" // Your measurementId
        ),
  );
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Robotic Gambit',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        brightness: Brightness.dark,
        elevatedButtonTheme: ElevatedButtonThemeData(
          style: ElevatedButton.styleFrom(
            foregroundColor: Colors.white, // Sets the text color on the button
            backgroundColor: Colors.blue, // The background color of the button
          ),
        ),
      ),
      home: SplashScreen(), // Directly navigating to SplashScreen
    );
  }
}