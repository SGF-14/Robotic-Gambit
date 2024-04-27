import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:intl/intl.dart';
import 'dart:math';
import 'splash_screen.dart';

class MatchScreen extends StatefulWidget {
  final String playerName;

  const MatchScreen({Key? key, required this.playerName}) : super(key: key);

  @override
  _MatchScreenState createState() => _MatchScreenState();
}

class _MatchScreenState extends State<MatchScreen> {
  late Timer _timerRobot;
  int _startRobot = 600;
  int _startPlayer = 600;
  DateTime? _startTime;

  @override
  void initState() {
    super.initState();
    startTimerRobot();
  }

Future<void> endPlayerTurn() async {
  try {
    var url = Uri.parse('https://roboticgambit.ngrok.app/end_turn');
    var response = await http.post(
      url,
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
    );

    if (response.statusCode == 200) {
      // Handle response data or update UI accordingly
      print("Turn ended successfully: ${response.body}");
    } else {
      // Error handling
      print('Failed to end turn with status code: ${response.statusCode}');
      print('Response body: ${response.body}');
      throw Exception('Failed to end turn');
    }
  } catch (e) {
    // Error handling
    print('Error ending turn: $e');
  }
}



  void startTimerRobot() {
    const oneSec = Duration(seconds: 1);
    _startTime = DateTime.now();
    _timerRobot = Timer.periodic(oneSec, (Timer timer) {
      if (_startRobot < 1) {
        timer.cancel();
      } else {
        setState(() {
          _startRobot--;
        });
      }
    });
  }

  String formatTime(int seconds) {
    final minutes = seconds ~/ 60;
    final remainingSeconds = seconds % 60;
    return '${minutes.toString().padLeft(2, '0')}:${remainingSeconds.toString().padLeft(2, '0')}';
  }

  void endGame(String result) async {
    final response = await http.post(
      Uri.parse('https://roboticgambit.ngrok.app/complete_chess_match'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(<String, String>{
        'match_id': 'your_match_id_here', 
      }),
    );

    if (response.statusCode == 200) {
      Navigator.pushAndRemoveUntil(
        context,
        MaterialPageRoute(builder: (context) => SplashScreen()),
        (Route<dynamic> route) => false,
      );
    } else {
    }
  }

  @override
  Widget build(BuildContext context) {
    double boardSize = MediaQuery.of(context).size.width * 0.8;
    return WillPopScope(
      onWillPop: () async {
        _timerRobot.cancel();
        return true;
      },
      child: Scaffold(
        backgroundColor: const Color.fromARGB(255, 31, 35, 39),
        body: SingleChildScrollView(
          child: Column(
            children: [
              SafeArea(
                child: Align(
                  alignment: Alignment.topLeft,
                  child: IconButton(
                    icon: const Icon(Icons.arrow_back, color: Colors.white),
                    onPressed: showSurrenderDialog,
                  ),
                ),
              ),
              Center(
                child: Image.network(
                  'https://i.ibb.co/VMxWZPW/logo.png',
                  width: 150,
                  height: 150,
                  errorBuilder: (context, error, stackTrace) => Text(
                      'Image not found',
                      style: TextStyle(color: Colors.white, fontSize: 9)),
                ),
              ),
              const SizedBox(height: 20),
              SizedBox(
                width: boardSize,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text('Robotic Gambit',
                        style: TextStyle(color: Colors.white, fontSize: 20)),
                    _buildTimerBox(formatTime(_startRobot)),
                  ],
                ),
              ),

              // chessboard part
              Container(
                width: boardSize,
                height: boardSize,
                decoration: BoxDecoration(
                  image: DecorationImage(
                    image: AssetImage('assets/styled_chess_board.png'),
                    fit: BoxFit.cover,

                // child: GridView.builder(
                //   physics: NeverScrollableScrollPhysics(),
                //   gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                //       crossAxisCount: 8),
                //   itemCount: 64,
                //   itemBuilder: (context, index) {
                //     bool isLightSquare = (index ~/ 8) % 2 == index % 2;
                //     return Container(
                //         color: isLightSquare
                //             ? Colors.grey[300]
                //             : Colors.grey[800]);
                
                  ),
                ),
              ),


              SizedBox(
                width: boardSize,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(widget.playerName,
                        style: TextStyle(color: Colors.white, fontSize: 20)),
                    _buildTimerBox(formatTime(_startPlayer)),
                  ],
                ),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.grey[850],
                  padding: EdgeInsets.symmetric(horizontal: 60, vertical: 20),
                  shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(5)),
                ),
                onPressed: endPlayerTurn,  // Call the function when the button is pressed
                child: Text('End Turn', style: TextStyle(fontSize: 18)),
              ),
              const SizedBox(height: 20),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildTimerBox(String time) {
    return Container(
      padding: EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
      decoration: BoxDecoration(
          color: Colors.grey[850], borderRadius: BorderRadius.circular(10)),
      child: Text(time, style: TextStyle(color: Colors.white, fontSize: 20)),
    );
  }

  void showSurrenderDialog() {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: Text('Surrender'),
        content: Text('Are you sure you want to surrender?'),
        actions: [
          TextButton(
            onPressed: () => Navigator.of(context).pop(),
            child: Text('Cancel'),
          ),
          TextButton(
            onPressed: () {
              endGame('Lose');
            },
            child: Text('Yes, surrender'),
          ),
        ],
      ),
    );
  }


  @override
  void dispose() {
    _timerRobot.cancel();
    super.dispose();
  }
}
