import 'package:flutter/material.dart';
import 'start_match_screen.dart'; // Ensure this file exists with your StartMatchScreen widget
import 'records_screen.dart'; // Ensure this file exists with your RecordsScreen widget

class SplashScreen extends StatelessWidget {
  const SplashScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 31, 35, 39),
      body: SafeArea(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: <Widget>[
            Expanded(
              flex: 2,
              child: Center(
                child: FractionallySizedBox(
                  widthFactor: 0.6,
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Image.network(
                        'https://i.ibb.co/sbTw6Lm/Gambit.png',
                        errorBuilder: (context, error, stackTrace) {
                          return const Text('Image not found',
                              style: TextStyle(color: Colors.white));
                        },
                      ),
                      const SizedBox(height: 8),
                      const Text(
                        'Train yourself by defeating yourself!',
                        textAlign: TextAlign.center,
                        style: TextStyle(color: Colors.grey, fontSize: 18),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            const SizedBox(height: 32),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 50),
              child: _buildElevatedButton(
                context,
                'Start Match',
                StartMatchScreen(),
              ),
            ),
            const SizedBox(height: 24),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 50),
              child: _buildElevatedButton(
                context,
                'See Records',
                RecordsScreen(),
              ),
            ),
            const Spacer(flex: 1),
          ],
        ),
      ),
    );
  }

  Widget _buildElevatedButton(
      BuildContext context, String title, Widget destination) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: const Color(0xFF2c3237), // Gray background color
          minimumSize: const Size.fromHeight(60),
          textStyle: const TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
              color: Colors.white), // Explicitly setting text color here
        ),
        onPressed: () => Navigator.push(
            context, MaterialPageRoute(builder: (context) => destination)),
        child: Text(
          title,
          style: const TextStyle(
              color: Colors.white), // Ensure text color is white
        ),
      ),
    );
  }
}
