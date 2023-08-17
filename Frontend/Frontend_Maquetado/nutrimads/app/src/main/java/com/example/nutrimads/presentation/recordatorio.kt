package com.example.nutrimads.presentation

import android.content.Intent
import android.os.Bundle
import android.view.View
import androidx.activity.ComponentActivity
import com.example.nutrimads.R

class recordatorio : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.recordatorio)
    }
    fun irARecordatorio2(view: View) {
        val intent = Intent(this, crearecordatorio::class.java)
        startActivity(intent)
    }
}