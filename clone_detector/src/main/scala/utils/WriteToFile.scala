package utils

import java.io.{File, PrintWriter}

class WriteToFile {
  def writeToFile(filename:String, string:String):Unit={
    val writer =new PrintWriter(new File(filename))
    writer.write(string)
    writer.close()
  }
}
