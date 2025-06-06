import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'match_screen.dart';  

class StartMatchScreen extends StatefulWidget {
  const StartMatchScreen({Key? key}) : super(key: key);

  @override
  State<StartMatchScreen> createState() => _StartMatchScreenState();
}

class _StartMatchScreenState extends State<StartMatchScreen> {
  final TextEditingController _nameController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color.fromARGB(255, 31, 35, 39),
      body: SafeArea(
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: Align(
                  alignment: Alignment.topLeft,
                  child: IconButton(
                    icon: const Icon(Icons.arrow_back, color: Colors.white),
                    onPressed: () => Navigator.of(context).pop(),
                  ),
                ),
              ),
              Center(
                child: FractionallySizedBox(
                  widthFactor: 0.6,
                  child: Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Hero(
                        tag: 'logo',
                        child: Image.network(
                          'https://i.ibb.co/VMxWZPW/logo.png',
                          errorBuilder: (context, error, stackTrace) {
                            return const Text('Image not found',
                                style: TextStyle(color: Colors.white));
                          },
                        ),
                      ),
                      const SizedBox(height: 8),
                      Hero(
                        tag: 'sub-text',
                        child: const Material(
                          color: Colors.transparent,
                          child: Text(
                            'Train yourself by defeating yourself!',
                            textAlign: TextAlign.center,
                            style: TextStyle(
                              color: Colors.grey,
                              fontSize: 18,
                            ),
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 32),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 50),
                child: TextField(
                  controller: _nameController,
                  decoration: const InputDecoration(
                    hintText: 'Enter your name',
                    fillColor: Colors.white,
                    filled: true,
                    border: OutlineInputBorder(),
                    hintStyle: TextStyle(fontSize: 18),
                  ),
                ),
              ),
              const SizedBox(height: 24),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 50),
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF2c3237),
                    minimumSize: const Size.fromHeight(60),
                    textStyle: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
                  ),
                  onPressed: () async {
                    if (_nameController.text.isEmpty) {
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text('Please enter your name to start.'))
                      );
                      return;
                    }

                    try {
                      final response = await http.post(
                        // Uri.parse('https://localhost:5000/start_match'), // local
                        Uri.parse('https://roboticgambit.ngrok.app/start_match'), // ngrokul
                        headers: <String, String>{
                          'Content-Type': 'application/json; charset=UTF-8',
                        },
                        body: jsonEncode(<String, String>{
                          'username': _nameController.text,
                        }),
                      );

                      print('Response status: ${response.statusCode}');
                      print('Response body: ${response.body}');

                      if (response.statusCode == 200) {
                        print('Match started successfully1');
                        Navigator.of(context).push(MaterialPageRoute(
                            builder: (context) => MatchScreen(playerName: _nameController.text)));
                        print('Match started successfully2');
                      } else {
                        print('Failed to start match: ${response.body}');
                        ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(content: Text('Failed to start match: ${response.body}'))
                        );
                      }

                    } catch (e) {
                      print('Error connecting to the server: $e');
                      ScaffoldMessenger.of(context).showSnackBar(
                        SnackBar(content: Text('Error connecting to the server: $e'))
                      );
                    }
                  },
                  child: const Text('Start', style: TextStyle(color: Colors.white)),
                ),
              ),
              const SizedBox(height: 16),
            ],
          ),
        ),
      ),
    );
  }
}
