import 'package:flutter/material.dart';


Widget Atombutton(String data, Function() f, Color C){
  return ElevatedButton(onPressed: f, child: Text(data));
}