import 'package:flutter/material.dart';
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
    _timerRobot.cancel();

    DateTime endTime = DateTime.now();
    Duration gameDuration = endTime.difference(_startTime!);
    String formattedDuration =
        "${gameDuration.inMinutes}:${(gameDuration.inSeconds % 60).toString().padLeft(2, '0')}";

    String formattedDate = DateFormat("MM/dd").format(DateTime.now());
    String matchID = Random().nextInt(900000).toString().padLeft(6, '0');

    FirebaseFirestore firestore = FirebaseFirestore.instance;
    CollectionReference recordsRef = firestore.collection('records');

    await recordsRef.add({
      'Date': formattedDate,
      'Duration': formattedDuration,
      'MatchID': matchID,
      'PGN': "Example PGN data",
      'Player': widget.playerName,
      'Result': result,
    });
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
              Container(
                width: boardSize,
                height: boardSize,
                child: GridView.builder(
                  physics: NeverScrollableScrollPhysics(),
                  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: 8),
                  itemCount: 64,
                  itemBuilder: (context, index) {
                    bool isLightSquare = (index ~/ 8) % 2 == index % 2;
                    return Container(
                        color: isLightSquare
                            ? Colors.grey[300]
                            : Colors.grey[800]);
                  },
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
                onPressed: () {}, // Button does nothing when pressed
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
              Navigator.of(context).pop();
              endGame('Lose');
              Navigator.pushAndRemoveUntil(
                context,
                MaterialPageRoute(builder: (context) => SplashScreen()),
                (Route<dynamic> route) => false,
              );
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
