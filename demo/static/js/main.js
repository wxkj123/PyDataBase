function calculate(){
    let a=document.getElementById('text1').value;
    let b=document.getElementById('text2').value;
    let c=document.getElementById('text3').value;
    pywebview.api.calculate(a,b,c).then(
        (value)=>{
            document.getElementById('result').innerHTML=('Result: '+value)
        }
    );
}
function clear_all(){
    document.getElementById('text1').value='';
    document.getElementById('text2').value='';
    document.getElementById('text3').value='';
}
document.getElementById('text3').addEventListener(
    'keydown',function(event){
        if (event.key=='Enter'||event.keyCode==13){
            calculate();
        }
    }
)