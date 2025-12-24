import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class DetailScreen extends StatelessWidget {
  // const DetailScreen({super.key});

  String pic;

  DetailScreen(this.pic);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("មុខម្ងូបលំអិត", style: GoogleFonts.freehand()),
        backgroundColor: Colors.pink,
        foregroundColor: Colors.white,
      ),
      body: Image.network(pic, fit: BoxFit.cover),
    );
  }
}
