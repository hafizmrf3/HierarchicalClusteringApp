import tkinter 
import tkinter.messagebox
import matplotlib.pyplot as plt  
import pandas as pd  
import numpy as np 
from tkinter import * 


def main():
    mainform = tkinter.Tk()
    mainform.title("Aplikasi Klasterisasi Hierarki")
    mainform.geometry("1200x700")
    mainform.configure(background='purple')
   
    lblMtd = tkinter.Label(mainform, fg="purple", font=("Candara", 20), text="Aplikasi Klasterisasi Hierarki" )
    lblMtd.pack()
    lblcopyright = tkinter.Label(mainform, fg="purple", font=("Candara", 10), text="copyright©2019sarmagSI16" )
    lblcopyright.pack()
   
    def item1click():
        plt.close('all') 
        tkinter.messagebox.showinfo("Informasi", "Metode yang dipilih adalah SingleLink (Minimum Distance)")        
        #label metode
        lblMtd['text'] = "Minimum Distance (Single Link)"
        lblMtd.pack()
        #meload dummy data de
        customer_data = pd.read_csv('H:/TGS_CLUSTERING/hierarchicalmethod/shopping_data.csv') 
        customer_data.shape
        customer_data.head()
        #seleksi data yang ingin digunakan
        data = customer_data.iloc[:, 3:5].values 
        #menampilkan dendogram
        import scipy.cluster.hierarchy as shc
        plt.figure(figsize=(5, 5))  
        plt.title("Customer Dendograms")  
        dend = shc.dendrogram(shc.linkage(data, method='single')) 
        #menampilkan cluster dari metode single
        from sklearn.cluster import AgglomerativeClustering
        cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='single')  
        cluster.fit_predict(data)  
        plt.figure(figsize=(5, 5))
        plt.title("Customer Scatterplot")  
        plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow')
        plt.show()

    def item2click():
        plt.close('all')    
        tkinter.messagebox.showinfo("Informasi", "Metode yang dipilih adalah MultiLink (Maximum Distance)")
        #label metode
        lblMtd['text'] = "Maximum Distance (Multi Link)"    
        lblMtd.pack()
        #meload dummy data 
        customer_data = pd.read_csv('H:/TGS_CLUSTERING/hierarchicalmethod/shopping_data.csv') 
        customer_data.shape
        customer_data.head()
        #seleksi data yang ingin digunakan
        data = customer_data.iloc[:, 3:5].values 
        #menampilkan dendogram
        import scipy.cluster.hierarchy as shc
        plt.figure(figsize=(5, 5))  
        plt.title("Customer Dendograms")  
        dend = shc.dendrogram(shc.linkage(data, method='complete')) 
        #menampilkan cluster dari metode complete
        from sklearn.cluster import AgglomerativeClustering
        cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='complete')  
        cluster.fit_predict(data)  
        plt.figure(figsize=(5, 5)) 
        plt.title("Customer Scatterplot") 
        plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow') 
        plt.show()
        

    def item3click():
        plt.close('all')
        tkinter.messagebox.showinfo("Informasi", "Metode yang dipilih adalah Centroid (Mean Distance)")
        #label metode
        lblMtd['text'] = "Mean Distance (Centroid)"
        lblMtd.pack()
        #meload dummy data 
        customer_data = pd.read_csv('H:/TGS_CLUSTERING/hierarchicalmethod/shopping_data.csv') 
        customer_data.shape
        customer_data.head()
        #seleksi data yang ingin digunakan
        data = customer_data.iloc[:, 3:5].values 
        #menampilkan dendogram
        import scipy.cluster.hierarchy as shc
        plt.figure(figsize=(5, 5))  
        plt.title("Customer Dendograms")  
        dend = shc.dendrogram(shc.linkage(data, method='ward')) 
        #menampilkan cluster dari metode centroid
        from sklearn.cluster import AgglomerativeClustering
        cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')  
        cluster.fit_predict(data)  
        plt.figure(figsize=(5, 5)) 
        plt.title("Customer Scatterplot")  
        plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow') 
        plt.show()

    def item4click():
        plt.close('all')
        tkinter.messagebox.showinfo("Informasi", "Metode yang dipilih adalah Group Average (Average Distance)")
        #label metode
        lblMtd['text'] = "Group Average (Average Distance)"
        lblMtd.pack()
        #meload dummy data 
        customer_data = pd.read_csv('H:/TGS_CLUSTERING/hierarchicalmethod/shopping_data.csv') 
        customer_data.shape
        customer_data.head()
        #seleksi data yang ingin digunakan
        data = customer_data.iloc[:, 3:5].values 
        #menampilkan dendogram
        import scipy.cluster.hierarchy as shc
        plt.figure(figsize=(5, 5))  
        plt.title("Customer Dendograms")  
        dend = shc.dendrogram(shc.linkage(data, method='average')) 
        #menampilkan cluster dari metode average
        from sklearn.cluster import AgglomerativeClustering
        cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='average')  
        cluster.fit_predict(data)  
        plt.figure(figsize=(5, 5))  
        plt.title("Customer Scatterplot") 
        plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow') 
        plt.show()

    def item5click():
        plt.close('all')
        tkinter.messagebox.showinfo("Informasi", "Metode yang dipilih adalah SSE (Ward's Method)")
        #label metode
        lblMtd['text'] = "SSE (Ward's Method)"
        lblMtd.pack()
        #meload dummy data 
        customer_data = pd.read_csv('H:/TGS_CLUSTERING/hierarchicalmethod/shopping_data.csv') 
        customer_data.shape
        customer_data.head()
        #seleksi data yang ingin digunakan
        data = customer_data.iloc[:, 3:5].values 
        #menampilkan dendogram
        import scipy.cluster.hierarchy as shc
        plt.figure(figsize=(5, 5))  
        plt.title("Customer Dendograms")  
        dend = shc.dendrogram(shc.linkage(data, method='ward')) 
        #menampilkan cluster dari metode ward
        from sklearn.cluster import AgglomerativeClustering
        cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')  
        cluster.fit_predict(data)  
        plt.figure(figsize=(5, 5))  
        plt.title("Customer Scatterplot") 
        plt.scatter(data[:,0], data[:,1], c=cluster.labels_, cmap='rainbow') 
        plt.show()

    def bantuan1click():
        tkinter.messagebox.showinfo("Informasi", "Cara Menggunakan Aplikasi : "
             + "\n 1. Pilih menu bar 'Pilih Metode' " 
             + "\n 2. Klik Metode yang ingin digunakan ")
    
    def bantuan2click():
        tkinter.messagebox.showinfo("Informasi", "Tentang Aplikasi :"
             + "\n - Aplikasi ini dibuat untuk menyelesaikan tugas matakuliah Data Mining mengenai Hierarchical Clustering" 
             + "\n - Dataset yang digunakan bersumber dari https://www.kaggle.com/bikram1505/shopping-data ")
    
    def keluarclick():
        exit()
    
   

    #membuat menubarnya
    menubar = tkinter.Menu(mainform)

    #membuat menu methode
    mtd = tkinter.Menu(menubar, tearoff=0)
    mtd.add_command(label="SingleLink", command=item1click)
    mtd.add_separator()
    mtd.add_command(label="MultiLink", command=item2click)
    mtd.add_separator()
    mtd.add_command(label="Centroid", command=item3click)
    mtd.add_separator()
    mtd.add_command(label="Group Average", command=item4click)
    mtd.add_separator()
    mtd.add_command(label="SSE", command=item5click)
    menubar.add_cascade(label="Pilih Metode", menu=mtd)

    #membuat menu bantuan 
    bantuan = tkinter.Menu(menubar, tearoff=0)
    bantuan.add_command(label="Penggunaan Aplikasi", command=bantuan1click)
    bantuan.add_separator()
    bantuan.add_command(label="Tentang Aplikasi", command=bantuan2click)
    bantuan.add_separator()
    bantuan.add_command(label="Keluar", command=keluarclick)
    menubar.add_cascade(label="Bantuan", menu=bantuan)

    #setting menubar
    mainform.config(menu=menubar)
    mainform.mainloop()


if __name__ == "__main__":
    main() 