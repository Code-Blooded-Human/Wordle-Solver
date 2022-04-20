class Box{
    constructor(name,letter='O'){
        this.name = name;
        this.color = '#eeeeee';
        this.colors = ['#eeeeee', '#29AB87', '#f1ff62']
        this.state = 0;
        let html = "<div class='box' id='"+name+"'>"+letter+"</div>";
        let box = this;
        
        $("#main-container").append(html);
        
        $("#"+name).click(()=>{
            box.state++;
            box.state=box.state%3;
            this.color = this.colors[this.state];
            $("#"+name).css('background-color',this.color);
        })
    }

    setValue(letter){
        $("#"+this.name).text(letter);
    }

    getColor(){
        if(this.state == 0){
            return 'b';
        }
        if(this.state == 1){
            return 'g'
        }
        if(this.state == 2){
            return 'y';
        }
        return 'x';
    }

    resetColor(){
        this.state=0;
        this.color = this.colors[this.state];
        $("#"+this.name).css('background-color',this.color);
    }
}

let box1 = new Box('box1','H');
let box2 = new Box('box2','E');
let box3 = new Box('box3','L');
let box4 = new Box('box4','L');
let box5 = new Box('box5','O');

function setValue(word){
    letters = word.split("");
    console.log(letters);
    box1.setValue(letters[0]);
    box2.setValue(letters[1]);
    box3.setValue(letters[2]);
    box4.setValue(letters[3]);
    box5.setValue(letters[4]);
}

function startGame(){
axios.get('http://127.0.0.1:5000/start')
  .then(function (response) {
    console.log(response);
    setValue(response.data.guess);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
}
function resetColor(){
    box1.resetColor();
    box2.resetColor();
    box3.resetColor();
    box4.resetColor();
    box5.resetColor();
}
function next(){
    let out = box1.getColor()+box2.getColor()+box3.getColor()+box4.getColor()+box5.getColor();
    console.log(out);
    resetColor();
    axios.get('http://127.0.0.1:5000/play?out='+out)
  .then(function (response) {
    console.log(response);
    setValue(response.data.guess);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  });
}

startGame();
console.log("JS running");