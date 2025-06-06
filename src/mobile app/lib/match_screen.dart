import 'package:flutter/material.dart' as mat;
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:async';
import 'package:cloud_firestore/cloud_firestore.dart' as firestore;
import 'package:intl/intl.dart';
import 'dart:math';
import 'splash_screen.dart';
import 'package:chess/chess.dart' as chess;
import 'package:flutter_chess_board/flutter_chess_board.dart';
import 'package:audioplayers/audioplayers.dart';

class MatchScreen extends mat.StatefulWidget {
  final String playerName;

  const MatchScreen({mat.Key? key, required this.playerName}) : super(key: key);

  @override
  _MatchScreenState createState() => _MatchScreenState();
}

class _MatchScreenState extends mat.State<MatchScreen> {
  late Timer _timerRobot;
  int _startRobot = 600;
  int _startPlayer = 600;
  DateTime? _startTime;
  ChessBoardController _controller = ChessBoardController();
  chess.Chess _chessGame = chess.Chess();
  AudioPlayer audioPlayer = AudioPlayer();

  @override
  void initState() {
    super.initState();
    startTimerRobot();
    _controller.game = _chessGame;
    playStartupSound();
  }

  Future<void> playStartupSound() async {
    await audioPlayer.play('assets/sounds/game-start.mp3');

}

  Future<void> endPlayerTurn() async {
    try {
      await audioPlayer.play('assets/sounds/move-self.mp3');
      var url = Uri.parse('https://roboticgambit.ngrok.app/end_turn');
      var response = await http.post(
        url,
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
      );

      if (response.statusCode == 200) {
        updateBoardFromBackend(); 
        print("Turn ended successfully: ${response.body}");
      } else {
        print('Failed to end turn with status code: ${response.statusCode}');
        print('Response body: ${response.body}');
        showIllegalMoveDialog();
      }
    } catch (e) {
      print('Error ending turn: $e');
      showIllegalMoveDialog();
    }
  }

  void showIllegalMoveDialog() {
  mat.showDialog(
    context: context,
    builder: (context) => mat.AlertDialog(
      title: mat.Text('Illegal Move'),
      content: mat.Text('Return your pieces to their previous normal position, then press "Ready".'),
      actions: [
        mat.TextButton(
          onPressed: () {
            mat.Navigator.of(context).pop();
            initialFrame(); 
          },
          child: mat.Text('Ready'),
        ),
      ],
    ),
  );
}

Future<void> initialFrame() async {
  var url = Uri.parse('https://roboticgambit.ngrok.app/initial_frame');
  var response = await http.post(
    url,
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
  );

  if (response.statusCode == 200) {
    
    print("recapture Initial frame: ${response.body}");
  } else {
    
    print('Failed to recapture initial frame with code: ${response.statusCode}');
    print('Response body: ${response.body}');
  }
}

  void updateBoardFromBackend() {
    String fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1";
    _chessGame.load(fen);
    setState(() {}); 
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
    await audioPlayer.play('assets/sounds/game-end.mp3');
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
      mat.Navigator.pushAndRemoveUntil(
        context,
        mat.MaterialPageRoute(builder: (context) => SplashScreen()),
        (mat.Route<dynamic> route) => false,
      );
    }
  }

  @override
  mat.Widget build(mat.BuildContext context) {
    double boardSize = mat.MediaQuery.of(context).size.width * 0.8;
    return mat.WillPopScope(
      onWillPop: () async {
        _timerRobot.cancel();
        return true;
      },
      child: mat.Scaffold(
        backgroundColor: mat.Color.fromARGB(255, 31, 35, 39),
        body: mat.SingleChildScrollView(
          child: mat.Column(
            children: [
              mat.SafeArea(
                child: mat.Align(
                  alignment: mat.Alignment.topLeft,
                  child: mat.IconButton(
                    icon: const mat.Icon(mat.Icons.arrow_back, color: mat.Colors.white),
                    onPressed: showSurrenderDialog,
                  ),
                ),
              ),
              mat.Center(
                child: mat.Image.network(
                  'https://i.ibb.co/VMxWZPW/logo.png',
                  width: 150,
                  height: 150,
                  errorBuilder: (context, error, stackTrace) => mat.Text(
                      'Image not found',
                      style: mat.TextStyle(color: mat.Colors.white, fontSize: 9)),
                ),
              ),
              const mat.SizedBox(height: 20),
              mat.SizedBox(
                width: boardSize,
                child: mat.Row(
                  mainAxisAlignment: mat.MainAxisAlignment.spaceBetween,
                  children: [
                    mat.Text('Robotic Gambit',
                        style: mat.TextStyle(color: mat.Colors.white, fontSize: 20)),
                    _buildTimerBox(formatTime(_startRobot)),
                  ],
                ),
              ),
              ChessBoard(
                controller: _controller,
                size: boardSize,
                onMove: () {
                },
              ),
              mat.SizedBox(
                width: boardSize,
                child: mat.Row(
                  mainAxisAlignment: mat.MainAxisAlignment.spaceBetween,
                  children: [
                    mat.Text(widget.playerName,
                        style: mat.TextStyle(color: mat.Colors.white, fontSize: 20)),
                    _buildTimerBox(formatTime(_startPlayer)),
                  ],
                ),
              ),
              const mat.SizedBox(height: 20),
              mat.ElevatedButton(
                style: mat.ElevatedButton.styleFrom(
                  backgroundColor: mat.Colors.grey[850],
                  padding: mat.EdgeInsets.symmetric(horizontal: 60, vertical: 20),
                  shape: mat.RoundedRectangleBorder(
                      borderRadius: mat.BorderRadius.circular(5)),
                ),
                onPressed: endPlayerTurn,
                child: mat.Text('End Turn', style: mat.TextStyle(fontSize: 18)),
              ),
              const mat.SizedBox(height: 20),
            ],
          ),
        ),
      ),
    );
  }

  mat.Widget _buildTimerBox(String time) {
    return mat.Container(
      padding: mat.EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
      decoration: mat.BoxDecoration(
          color: mat.Colors.grey[850], borderRadius: mat.BorderRadius.circular(10)),
      child: mat.Text(time, style: mat.TextStyle(color: mat.Colors.white, fontSize: 20)),
    );
  }

  void showSurrenderDialog() {
    mat.showDialog(
      context: context,
      builder: (context) => mat.AlertDialog(
        title: mat.Text('Surrender'),
        content: mat.Text('Are you sure you want to surrender?'),
        actions: [
          mat.TextButton(
            onPressed: () => mat.Navigator.of(context).pop(),
            child: mat.Text('Cancel'),
          ),
          mat.TextButton(
            onPressed: () {
              endGame('Lose');
            },
            child: mat.Text('Yes, surrender'),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    _timerRobot.cancel();
    audioPlayer.dispose();
    super.dispose();
  }
}