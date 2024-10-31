import 'package:app1/atomic/atoms/AtomButton.dart';
import 'package:app1/atomic/molecules/MolAppBar.dart';
import 'package:app1/atomic/utils/routes.dart';
import 'package:flutter/material.dart';

class Homepage extends StatelessWidget {
  const Homepage
({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Center(child: Text("Home"),),),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Center(child: Atombutton("Criar via Prompts", () => {
            Navigator.of(context).pushNamed(Routes.prompts.name)
          }, Colors.purple.shade500 ),),

          SizedBox(height: 10),

          Center(child: Atombutton("Criar via Imagens", () => {
            Navigator.of(context).pushNamed(Routes.AddImagesPage.name)
          }, Colors.purple.shade500 ),)
        ],
      ),
    );
  }
}