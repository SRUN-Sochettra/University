import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'foodmodel.dart';

class DetailScreen extends StatelessWidget {
  // const DetailScreen({super.key});

  Food item;

  DetailScreen(this.item);

  @override
  Widget build(BuildContext context) {
    int rielPrice = (item.price * 4000).toInt();

    return Scaffold(
      appBar: AppBar(
        title: Text("មុខម្ងូបលំអិត", style: GoogleFonts.freehand()),
        backgroundColor: Colors.pink,
        foregroundColor: Colors.white,
      ),
      body: ListView(
        children: [
          Image.network(item.image, fit: BoxFit.cover),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              item.title,
              style: GoogleFonts.metal(fontSize: 20),
              textAlign: TextAlign.center,
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "${item.price} USD ($rielPrice រៀល)",
              style: GoogleFonts.metal(fontSize: 20),
              textAlign: TextAlign.center,
            ),
          ),
        ],
      ),
    );
  }
}
