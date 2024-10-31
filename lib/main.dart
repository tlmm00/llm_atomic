import 'package:app1/atomic/atoms/AtomButton.dart';
import 'package:app1/atomic/pages/HomePage.dart';
import 'package:app1/atomic/pages/PromptPage.dart';
import 'package:app1/atomic/pages/DownloadPage.dart';
import 'package:app1/atomic/pages/AddImagesPage.dart';
import 'package:app1/atomic/pages/PreviewPage.dart';
import 'package:app1/atomic/utils/routes.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyWidget());
}

class MyWidget extends StatelessWidget {
  const MyWidget({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      //theme: ThemeData(),
      home: Homepage(),
      routes: {
        Routes.AddImagesPage.name: (context) => AddImagesPage(),
        Routes.preview.name: (context) => PreviewPage(),
        Routes.download.name: (context) => DownloadPage(),
        Routes.prompts.name: (context) => PromptPage()
      },
    );
  }
}

