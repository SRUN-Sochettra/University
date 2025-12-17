import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class FirstScreen extends StatelessWidget {
  List<String> foods = [
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://i.ytimg.com/vi/_12mKQnk4ik/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLDLMiOV2ejY7j_MbsqLmXhUd-tR-Q",
    "https://i.ytimg.com/vi/FcMGJGvOBcI/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBH7iEZ059SQ8otKVvXhqNjOWNcdA",
    "https://refile.tnaot.com/video/2018/10/6/2dba94dc452a432c8e28b31be9bda545.jpg?x-oss-process=image/watermark,image_RS5wbmc_eC1vc3MtcHJvY2Vzcz1pbWFnZS9yZXNpemUsUF8yMA,x_10,y_10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgpiNyLY39N1hDRYx2_K9OWBzhy1__dhmnSg&s",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
    "https://s9.kh1.co/4a/4a00f7f022977efa4aee26726ac41ace0bca0fc2.jpg",
  ];
  final pic1 =
      "https://preview.redd.it/i-think-i-figured-out-why-dr-doom-will-look-like-tony-stark-v0-1d2ybzom0xxe1.jpeg?auto=webp&s=137d9748dff7a617ed766120adfefd29176726b6";
  final pic2 =
      "https://mediaproxy.tvtropes.org/width/1200/https://static.tvtropes.org/pmwiki/pub/images/spider_man_1_1_4.png";

  FirstScreen({super.key});

  Widget _buildListViewBuilder1() {
    return ListView.builder(
      physics: BouncingScrollPhysics(),
      itemCount: foods.length,
      itemBuilder: (context, index) {
        return Padding(
          padding: const EdgeInsets.all(8.0),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(16),
            child: Image.network(foods[index], fit: BoxFit.cover, height: 200),
          ),
        );
      },
    );
  }

  Widget _buildGridViewBuilder() {
    return GridView.builder(
      physics: BouncingScrollPhysics(),
      padding: EdgeInsets.all(8),
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisCount: 2,
        childAspectRatio: 3 / 2,
        mainAxisSpacing: 8,
        crossAxisSpacing: 8,
      ), // SliverGridDelegateWithFixedCrossAxisCount
      itemCount: foods.length,
      itemBuilder: (context, index) {
        return ClipRRect(
          borderRadius: BorderRadius.circular(8),
          child: Image.network(foods[index], fit: BoxFit.cover),
        );
      },
    ); // GridView.builder
  }

  Widget _buildGridViewExtent() {
    return GridView.extent(
      scrollDirection: Axis.vertical, //.horizontal
      padding: EdgeInsets.all(8),
      physics: BouncingScrollPhysics(),
      // crossAxisCount: 3,
      maxCrossAxisExtent: 100,
      childAspectRatio: 3 / 5,
      mainAxisSpacing: 5,
      crossAxisSpacing: 10,
      children: [
        Container(width: 150, height: 190, color: Colors.amber),
        Container(width: 180, height: 100, color: Colors.pink),
        Container(width: 170, height: 130, color: Colors.blue),
        Container(width: 180, height: 150, color: Colors.lime),
        Container(width: 140, height: 190, color: Colors.purple),
        Container(width: 150, height: 190, color: Colors.amber),
        Container(width: 180, height: 100, color: Colors.pink),
        Container(width: 170, height: 130, color: Colors.blue),
        Container(width: 180, height: 150, color: Colors.lime),
        Container(width: 140, height: 190, color: Colors.purple),
        Container(width: 150, height: 190, color: Colors.amber),
        Container(width: 180, height: 100, color: Colors.pink),
        Container(width: 170, height: 130, color: Colors.blue),
        Container(width: 180, height: 150, color: Colors.lime),
        Container(width: 140, height: 190, color: Colors.purple),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: _buildGridViewBuilder(),
      backgroundColor: Colors.white,
      appBar: AppBar(
        title: Text("ម្ហូបខ្មែរ", style: GoogleFonts.moulpali()),
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
      floatingActionButtonLocation: FloatingActionButtonLocation.endFloat,
      floatingActionButton: FloatingActionButton(
        shape: CircleBorder(),
        backgroundColor: Colors.pink,
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
