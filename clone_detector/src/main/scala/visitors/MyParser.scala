package visitors
import java.io.File

import utils._

object MyApp {
  def main(strings: Array[String]): Unit = {
    val visitor = new MyVisitor()
    val w = new WriteToFile()
    val findOriginCode = new FindOriginCode()
    var args = ""
    var fileName = ""
    var ids = ""
    if (strings.length < 2) {
      println("Insufficient parameters")
    } else if (strings.length == 2) {
      args = strings(0)
      fileName = strings(1)
    } else {
      args = strings(0)
      fileName = strings(1)
      ids = strings(2)
    }
    parse_file(new File(fileName), visitor)
    if (args.equals("-identifier")) {
      w.writeToFile("sample-training-file.txt",visitor.identifierResult)
    } else if (args.equals("-AST")) {
      w.writeToFile("sample-training-file.txt", visitor.ASTResult)
    } else if (args.equals("-find-source-code")) {
      findOriginCode.findOriginCode(ids, visitor.sourceMethodCode, visitor.sourceFileName)    //Find the source code based on the result id
    }
  }
  def parse_file(file: File,p:MyVisitor): Unit = {
    if (file.isFile && file.getName.endsWith(".scala")&&(!file.getAbsolutePath().contains("/test/"))) {
      p.temName=file.getAbsolutePath
      println(p.temName)
      p.parse(file.getAbsolutePath)
    } else if (file.isDirectory) {
      for (subFile <- file.listFiles()) {
        parse_file(subFile,p)
      }
    }


  }

}