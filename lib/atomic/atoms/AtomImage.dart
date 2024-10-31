import 'dart:io';

import 'package:flutter/material.dart';

Widget AtomImage(void Function() onTap, List<File?> imgList,int index) {
  return GestureDetector(
    onTap: onTap,
    child: imgList[index] == null || imgList.isEmpty
        ? Container(
            width: 100,
            height: 100,
            decoration: BoxDecoration(
              color: Colors.grey,
              borderRadius: BorderRadius.circular(8),
            ),
            child: Icon(
              Icons.add,
              size: 100,
            ),
          )
        : ClipRRect(
            borderRadius: BorderRadius.circular(8),
            child: Image.file(
              imgList[index]!,
              width: 100,
              height: 100,
              fit: BoxFit.cover,
            ),
          ),
  );
}
