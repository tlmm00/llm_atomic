import 'dart:io';

import 'package:app1/atomic/models/Prompt.dart';
import 'package:app1/atomic/molecules/MolCard.dart';
import 'package:app1/atomic/molecules/MolChat.dart';
import 'package:app1/atomic/utils/routes.dart';
import 'package:flutter/material.dart';

class PromptPage extends StatefulWidget {
  @override
  _PromptPageState createState() => _PromptPageState();
}

class _PromptPageState extends State<PromptPage> {
  final TextEditingController _controller = TextEditingController();
  final List<Prompt> _prompts = [];

  //TODO: Mostrar imagens dos layouts no chat
  //List<File> imgs = [];

  bool _IsLoading = false;

  Future<void> _sendPrompt() async {
    if (_controller.text.isEmpty) return;

    setState(() {
      _prompts.add(Prompt(
        text: _controller.text,
        isUserMessage: true,
      ));
    });

    _controller.clear();

    //mostra a progressbar
    _IsLoading = true;

    //realiza chamada assincrona para api
    await Future.delayed(Duration(seconds: 3));

    //esconde a progressbar
    _IsLoading = false;

    setState(() {
      //recebe os dados e devolve o codigo

      _prompts.add(Prompt(
        text: "Codigo aqui...",
        isUserMessage: false,
      ));
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Crie um Layout"),
        backgroundColor: Colors.purple.shade500,
        foregroundColor: Colors.white,
        actions: [
          //TODO: baixar o codigo
          IconButton(
            onPressed: () {
              Navigator.of(context).pushNamed(Routes.download.name);
            },
            icon: Icon(Icons.download),
          ),
        ],
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: _prompts.length,
              itemBuilder: (context, index) {
                final prompt = _prompts[index];
                return _IsLoading
                    ? LinearProgressIndicator()
                    : MolChat(prompt: prompt);
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: InputDecoration(
                      hintText: "Digite algo...",
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(16),
                      ),
                    ),
                  ),
                ),
                TextButton(onPressed: _sendPrompt, child: Text("Criar"))
              ],
            ),
          ),
        ],
      ),
    );
  }
}
