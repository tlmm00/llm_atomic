import 'package:app1/atomic/atoms/AtomButton.dart';
import 'package:app1/atomic/molecules/MolAppBar.dart';
import 'package:flutter/material.dart';

class DownloadPage extends StatelessWidget {
  const DownloadPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:
          MolAppBar("Download", Colors.purple.shade500 , () => Navigator.of(context).pop()),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.end,
    
        children: [
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: Center(
              child: Atombutton("Baixar Projeto",
                  () => {Navigator.of(context).pop()}, Colors.purple.shade500),
            ),
          )
        ],
      ),
    );
  }
}
