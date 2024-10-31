import 'dart:io';

import 'package:app1/atomic/atoms/AtomButton.dart';
import 'package:app1/atomic/molecules/MolAppBar.dart';
import 'package:app1/atomic/utils/routes.dart';
import 'package:flutter/material.dart';

class PreviewPage extends StatelessWidget {
  const PreviewPage({super.key});

  @override
  Widget build(BuildContext context) {
    final List<File?> imgs =
        ModalRoute.of(context)!.settings.arguments as List<File?>;

    return Scaffold(
      appBar: MolAppBar(
          "Preview", Colors.purple.shade500, () => {Navigator.of(context).pop()}),
      body: Column(children: [
        
        Expanded(
          child: PageView.builder(
            itemCount: imgs.length,
            itemBuilder: (context, index) {
              final img = imgs[index];
              return img != null
                  ? Image.file(
                      img,
                      fit: BoxFit.contain,
                      width: 50,
                      height: 50,
                    )
                  : Center(
                      child: Container(
                        width: 100,
                        height: 100,
                        color: Colors.grey,
                        child: Icon(Icons.image, size: 50),
                      ),
                    );
            },
          ),
        ),
        
        Padding(
          padding: EdgeInsets.all(16),
          child: Center(
            child: Atombutton(
                "Gerar projeto",
                () => {Navigator.of(context).pushNamed(Routes.download.name)},
                Colors.purple.shade500),
          ),
        ),
      ]),
    );
  }
}
