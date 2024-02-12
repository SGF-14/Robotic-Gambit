import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

import 'package:robotic_gambit/main.dart';

void main() {
  testWidgets('Splash screen buttons test', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(MyApp());

    // Verify that our buttons are present.
    expect(find.text('Start Match'), findsOneWidget);
    expect(find.text('See Records'), findsOneWidget);
  });
}
