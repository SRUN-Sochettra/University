import 'package:flutter/material.dart';

class FirstScreen extends StatelessWidget {
  // const FirstScreen({super.key});

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
        title: Text("First Screen"),
        backgroundColor: Colors.pink,
        foregroundColor: Colors.white,
      ),
      endDrawer: Drawer(backgroundColor: Colors.pink.shade700),
      drawer: Drawer(width: 350, child: Image.network(pic2, fit: BoxFit.cover)),
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
