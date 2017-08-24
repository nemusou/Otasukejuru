package jp.ict.muffin.otasukejuru

import android.os.CountDownTimer
import android.widget.TextView

/**
 * Created by mito on 2017/08/24.
 */
class CountDown: CountDownTimer {
    private val timerText: TextView
    
    constructor(millisUntilFinished: Long, countDownInterval: Long, timerText: TextView) : super(millisUntilFinished, countDownInterval) {
        this.timerText = timerText
    }
    
    override fun onFinish() {
        timerText.text = "0:00.000"
    }
    
    override fun onTick(millisUntilFinished: Long) {
        val m = millisUntilFinished / 1000 / 60
        val s = millisUntilFinished / 1000 % 60
        val ms = millisUntilFinished - s * 1000 - m * 1000 * 60
        
        timerText.text = String.format("%1$02d:%2$02d.%3$03d", m, s, ms)
    }
}