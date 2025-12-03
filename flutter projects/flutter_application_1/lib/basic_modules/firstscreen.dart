import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class FirstScreen extends StatelessWidget {
  final pic1 =
      "https://preview.redd.it/i-think-i-figured-out-why-dr-doom-will-look-like-tony-stark-v0-1d2ybzom0xxe1.jpeg?auto=webp&s=137d9748dff7a617ed766120adfefd29176726b6";
  final pic2 =
      "https://mediaproxy.tvtropes.org/width/1200/https://static.tvtropes.org/pmwiki/pub/images/spider_man_1_1_4.png";

  const FirstScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      appBar: AppBar(
        title: Text("កម្មវិធីដំបូងរបស់ខ្ញុំ", style: GoogleFonts.moulpali()),
        backgroundColor: Colors.pink,
        foregroundColor: Colors.white,
      ),
      endDrawer: Drawer(backgroundColor: Colors.pink.shade700),
      drawer: Drawer(
        backgroundColor: Colors.yellow.shade50,
        child: ListView(
          children: [
            DrawerHeader(child: Icon(Icons.face, size: 100)),
            ListTile(
              leading: Icon(Icons.home),
              title: Text("ទំព័រដើម"),
              subtitle: Text("Go to home page"),
              trailing: Icon(Icons.arrow_forward),
            ),
            ListTile(
              leading: Icon(Icons.settings),
              title: Text("ការកំណត់"),
              subtitle: Text("Go to settings"),
              trailing: Icon(Icons.arrow_forward),
            ),
            ListTile(
              leading: Icon(Icons.logout),
              title: Text("ចាកចេញ"),
              subtitle: Text("Logout"),
              trailing: Icon(Icons.arrow_forward),
            ),
          ],
        ),
      ),
      body: Center(child: Image.network(pic1)),
      floatingActionButtonLocation: FloatingActionButtonLocation.centerTop,
      floatingActionButton: FloatingActionButton(
        shape: CircleBorder(),
        backgroundColor: Colors.yellow,
        foregroundColor: Colors.black,
        onPressed: () {},
        child: Icon(Icons.person),
      ),
      bottomNavigationBar: BottomAppBar(
        color: Colors.yellow,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            IconButton(onPressed: () {}, icon: Icon(Icons.home)),
            IconButton(onPressed: () {}, icon: Icon(Icons.search)),
            IconButton(onPressed: () {}, icon: Icon(Icons.bookmark)),
            IconButton(onPressed: () {}, icon: Icon(Icons.more_horiz)),
          ],
        ),
      ),
    );
  }
}
