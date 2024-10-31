import 'dart:io';
import 'dart:typed_data';

import 'package:app1/atomic/atoms/AtomButton.dart';
import 'package:app1/atomic/atoms/AtomImage.dart';
import 'package:app1/atomic/molecules/MolAppBar.dart';
import 'package:app1/atomic/utils/routes.dart';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

class AddImagesPage extends StatefulWidget {
  const AddImagesPage({super.key});

  @override
  State<AddImagesPage> createState() => _AddImagesPageState();
}

class _AddImagesPageState extends State<AddImagesPage> {
  //File? _image;
  final List<File?> _imgs = List<File?>.filled(3, null);

  Future<XFile?> pickImage(int index) async {

    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: ImageSource.gallery);

    if (pickedFile != null) {
      setState(() {
        File _image = File(pickedFile.path);
        _imgs[index] = _image;
      });
    } else {
      print('Nenhuma imagem selecionada.');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: MolAppBar("Selecione as imagens", Colors.purple.shade500, () => Navigator.of(context).pop()),
      
      //TODO: Transformar isso em uma lista dinamica 
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceAround,
            children: [
              AtomImage(() => pickImage(0), _imgs,0),
              AtomImage(() => pickImage(1), _imgs,1),
              AtomImage(() => pickImage(2), _imgs,2),
            ],
          ),
          
          SizedBox(height: 100),

          Center(
            child: Atombutton(
                "Gerar projeto",
                () => { Navigator.pushNamed(
                  context,
                  Routes.preview.name,
                  arguments: _imgs,
                  )
                  },
                Colors.purple.shade500),
          )

        ],
      ),
    );
  }
}
