package com.example.nutrimads.presentation

import android.content.Intent
import android.os.Bundle
import android.view.View
import androidx.activity.ComponentActivity
import com.example.nutrimads.R

class recomendaciones : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.recomendaciones)
    }
    fun irARecomendacion(view: View) {
        val intent = Intent(this, recomendacion::class.java)
        startActivity(intent)
    }
}