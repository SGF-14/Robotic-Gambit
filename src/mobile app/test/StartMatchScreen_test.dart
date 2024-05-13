import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import '../lib/start_match_screen.dart';

void main() {
  testWidgets('Match does not start without entering name', (WidgetTester tester) async {
    await tester.pumpWidget(MaterialApp(home: StartMatchScreen()));

    // Attempt to find the Start button and tap it.
    var startButton = find.widgetWithText(ElevatedButton, 'Start');
    await tester.tap(startButton);

    // Rebuild the widget with the new state.
    await tester.pump();

    // Check if the SnackBar shows up with the correct text.
    expect(find.text('Please enter your name to start.'), findsOneWidget);
  });
}
