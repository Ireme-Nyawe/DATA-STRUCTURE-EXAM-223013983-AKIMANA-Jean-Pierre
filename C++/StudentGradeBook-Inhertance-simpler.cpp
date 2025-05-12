#include <iostream>
#include <vector>
using namespace std;

// Base class
class Student {
protected:
    string name;
    string studentID;
    vector<int> grades;

public:
    Student(string n, string id) {
        name = n;
        studentID = id;
    }

    void addGrade(int grade) {
        grades.push_back(grade);
    }

    float computeGPA() {
        if (grades.empty()) return 0.0;
        int sum = 0;
        for (int g : grades) sum += g;
        return static_cast<float>(sum) / grades.size();
    }

    virtual void displayInfo() {
        cout << "Name: " << name << "\nID: " << studentID << "\nGrades: ";
        for (int g : grades) cout << g << " ";
        cout << "\nGPA: " <<computeGPA() << "\n--------------------------\n";
    }

    virtual ~Student() {
    cout<<"space released";
    }  // Virtual destructor to clean up properly
};

// UGStudent inherits Student (hierarchical)
class UGStudent : public Student {
public:
    UGStudent(string n, string id) : Student(n, id) {}

    void displayInfo() override {
        cout << "[Undergraduate Student]\n";
        Student::displayInfo();
    }
};

// PGStudent inherits Student (hierarchical)
class PGStudent : public Student {
public:
    PGStudent(string n, string id) : Student(n, id) {}

    void displayInfo() override {
        cout << "[Postgraduate Student]\n";
        Student::displayInfo();
    }
};

// ResearchStudent inherits PGStudent (multilevel)
class ResearchStudent : public PGStudent {
public:
    ResearchStudent(string n, string id) : PGStudent(n, id) {}

    void displayInfo() override {
        cout << "[Research Student]\n";
        Student::displayInfo();
    }
};

// GradeSystem manages all students (hybrid)
class GradeSystem {
private:
    vector<Student*> students;

public:
    void addStudent(Student* s) {
        students.push_back(s);
    }

    void displayAll() {
        cout << "\n--- Student Gradebook Overview ---\n";
        for (auto s : students) {
            s->displayInfo();
        }
    }

    ~GradeSystem() {
        // Free memory for all students
        for (auto s : students) {
            delete s;
        }
    }
};

// Main
int main() {
    GradeSystem system;

    Student* s1 = new UGStudent("Mukiza Bertin", "UG001");
    s1->addGrade(85); s1->addGrade(90); s1->addGrade(78);
    system.addStudent(s1);

    Student* s2 = new PGStudent("Mucyo Clement", "PG001");
    s2->addGrade(92); s2->addGrade(88);
    system.addStudent(s2);

    Student* s3 = new ResearchStudent("Muhire Kelly", "RS001");
    s3->addGrade(70); s3->addGrade(75); s3->addGrade(80);
    system.addStudent(s3);

    system.displayAll();

    return 0;
}
