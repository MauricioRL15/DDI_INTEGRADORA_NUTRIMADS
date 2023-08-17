package com.example.nutrimads.presentation

import android.content.Intent
import android.os.Bundle
import android.view.View
import androidx.activity.ComponentActivity
import com.example.nutrimads.R

class crearecordatorio: ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.crearecordatorio)
    }
    fun irAMenu(view: View) {
        val intent = Intent(this, menu::class.java)
        startActivity(intent)
    }



}