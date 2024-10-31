import 'dart:io';

import 'package:flutter/material.dart';

Widget MolCard(List<File> imgs){

  return Expanded(
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
        );
}