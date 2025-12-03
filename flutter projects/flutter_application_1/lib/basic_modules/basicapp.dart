import 'package:flutter/material.dart';
import 'firstscreen.dart';

class BasicApp extends StatelessWidget {
  const BasicApp({super.key});

  //const MyWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(home: FirstScreen());
  }
}
