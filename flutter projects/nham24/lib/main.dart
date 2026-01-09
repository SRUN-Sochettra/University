
  // lib/main.dart
  import 'package:flutter/material.dart';
  import 'package:dynamic_color/dynamic_color.dart';
  import 'package:google_fonts/google_fonts.dart';
  import 'screens.dart';

  void main() {
    WidgetsFlutterBinding.ensureInitialized();
    runApp(const Nham24App());
  }

  class Nham24App extends StatefulWidget {
    const Nham24App({super.key});

    @override
    State<Nham24App> createState() => _Nham24AppState();
  }

  class _Nham24AppState extends State<Nham24App> {
    // ✅ Create ONE cart for the whole app (persists across all routes)
    final CartModel _cart = CartModel();

    // Brand seed color (purple)
    static const Color _seed = Color(0xFF7C3AED);

    @override
    Widget build(BuildContext context) {
      return DynamicColorBuilder(
        builder: (ColorScheme? lightDynamic, ColorScheme? darkDynamic) {
          final lightScheme = lightDynamic ?? ColorScheme.fromSeed(seedColor: _seed);
          final darkScheme = darkDynamic ??
              ColorScheme.fromSeed(
                seedColor: _seed,
                brightness: Brightness.dark,
              );

          return CartScope(
            cart: _cart, // ✅ CartScope ABOVE MaterialApp (so routes can see it)
            child: MaterialApp(
              title: 'Food Delivery App',
              debugShowCheckedModeBanner: false,
              themeMode: ThemeMode.system,
              theme: ThemeData(
                useMaterial3: true,
                colorScheme: lightScheme,
                textTheme: GoogleFonts.kantumruyProTextTheme(),
              ),
              darkTheme: ThemeData(
                useMaterial3: true,
                colorScheme: darkScheme,
                textTheme: GoogleFonts.kantumruyProTextTheme(),
              ),
              home: const MainScaffold(),
            ),
          );
        },
      );
    }
  }
