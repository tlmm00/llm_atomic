import 'package:flutter/material.dart';

AppBar MolAppBar(String data,Color C, Function() f){
  return AppBar(
    title: Text(data),
    leading: IconButton(onPressed: f, icon: Icon(Icons.arrow_back) ) ,
    backgroundColor: C,
    foregroundColor: Colors.white,
  );
}
