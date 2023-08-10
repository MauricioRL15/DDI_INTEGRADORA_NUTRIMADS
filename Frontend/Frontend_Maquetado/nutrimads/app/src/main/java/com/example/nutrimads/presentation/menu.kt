package com.example.nutrimads.presentation

import android.content.Intent
import android.os.Bundle
import android.view.View
import androidx.activity.ComponentActivity
import com.example.nutrimads.R

class menu : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.menu)
    }
    fun irABuscador(view: View) {
        val intent = Intent(this, buscadoralimentos::class.java)
        startActivity(intent)
    }
    fun irAContador(view: View) {
        val intent = Intent(this, contador::class.java)
        startActivity(intent)
    }
    fun irARecordatorio(view: View) {
        val intent = Intent(this, recordatorio::class.java)
        startActivity(intent)
    }
    fun irARecomendaciones(view: View) {
        val intent = Intent(this, recomendaciones::class.java)
        startActivity(intent)
    }
    fun irAAsistente(view: View) {
        val intent = Intent(this, asistente::class.java)
        startActivity(intent)
    }
    fun irAAcercade(view: View) {
        val intent = Intent(this, acercade::class.java)
        startActivity(intent)
    }
}